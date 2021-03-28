## direct operation
* greet
  - utter_greet
* operation
  - utter_affirm
  - form_info
  - form{"name": "form_info"}
  - form{"name": null}
  - utter_doing_task
  - utter_did_that_help
* affirm
  - utter_goodbye

## direct operation 2
* greet
  - utter_greet
* operation
  - utter_affirm
  - form_info
  - form{"name": "form_info"}
  - form{"name": null}
  - utter_doing_task
  - utter_did_that_help
* deny
  - utter_task_list
* operation
  - utter_affirm
  - form_info
  - form{"name": "form_info"}
  - form{"name": null}
  - utter_doing_task
  - utter_did_that_help
* affirm
  - utter_goodbye


## indirect operation
* greet
  - utter_greet
* machine_learning
  - utter_task_list
* operation
  - utter_affirm
  - form_info
  - form{"name": "form_info"}
  - form{"name": null}
  - utter_doing_task
  - utter_did_that_help
* affirm
  - utter_goodbye

## indirect operation 2
* greet
  - utter_greet
* machine_learning
  - utter_task_list
* operation
  - utter_affirm
  - form_info
  - form{"name": "form_info"}
  - form{"name": null}
  - utter_doing_task
  - utter_did_that_help
* deny
  - utter_task_list
* operation
  - utter_affirm
  - form_info
  - form{"name": "form_info"}
  - form{"name": null}
  - utter_doing_task
  - utter_did_that_help
* affirm
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## greet and goodbye
* greet
  - utter_greet
* goodbye
  - utter_goodbye
