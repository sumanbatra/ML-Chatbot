# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/



from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
import azureml.core
from azureml.core import Workspace
import azureml.core
from azureml.core import Workspace
from azureml.train.automl import AutoMLConfig
import pandas as pd
from sklearn.model_selection import train_test_split
from azureml.core.experiment import Experiment
from azureml.widgets import RunDetails

class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "action_hello_world"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return []

class ActionFormInfo(FormAction):
    def name(self) -> Text:
        """Unique identifier of the form"""
        return "form_info"
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["data", "column_name"]

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any],) -> List[Dict]:
        """Define what the form has to do
        after all required slots are filled"""
        task=tracker.get_slot('task')
        data=tracker.get_slot('data')
        column_name=tracker.get_slot('column_name')
        dispatcher.utter_message(template="utter_doing_task", task=tracker.get_slot('task'),data=tracker.get_slot('data'),
                                 column_name=tracker.get_slot('column_name'))
        # Load the workspace from the saved config file
        ws = Workspace.from_config()
        print('Ready to use Azure ML {} to work with {}'.format(azureml.core.VERSION, ws.name))

        
        df = pd.read_csv(data)
        train_data, test_data = train_test_split(df, test_size=0.1, random_state=42)
        label = column_name
        automl_config = AutoMLConfig(name='Automated ML Experiment',
                             task= task,
                             compute_target='local',
                             training_data = train_data,
                             validation_data = test_data,
                             label_column_name= label,
                             experiment_timeout_minutes=30,
                             iterations=6,
                             primary_metric = 'AUC_weighted',
                             featurization='auto',
                             )
        automl_experiment = Experiment(ws, 'mslearn-diabetes-automl')
        automl_run = automl_experiment.submit(automl_config)
        best_run, fitted_model = automl_run.get_output()
        best_run_metrics = best_run.get_metrics()
        metric_list = []
        for metric_name in best_run_metrics:
            metric = best_run_metrics[metric_name]
            metric_list.append((metric_name, metric))
        return fitted_model, metric_list
        
        print("The best model pipeline for the data is")
        dispatcher.utter_message(text="The best model pipeline for the data is")
        print(model)
        dispatcher.utter_message(model)
        print("The different metrics are")
        dispatcher.utter_message(text="The different metrics are")
        print(metrics)
        dispatcher.utter_message(text=metrics)
                             column_name=tracker.get_slot('column_name'))
        
        return []
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "data": [self.from_entity(entity="data", intent='operation'),
                     self.from_text()],
            "column_name": [self.from_entity(entity="column_name", intent="operation"),
                        self.from_text()],
        }

