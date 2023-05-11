# PHEE Dataset Instruction

## Description
We provide data of two formats: brat-format data for human visualisation and json-format data for machine processing. 

## Folder Structure
- clean: brat-format data
  train/dev/test:   
    *.ann: annotation file
    *.txt: text file
- json: json-format data
  - train.json: json-format data in the training set.
  - dev.json: json-format data in the devlopment set.
  - test.json: json-format data in the test set.

## Data format
### brat-format data
    - .txt: sentence text. A file only includes one sentence.
    - .ann: each line includes the information of an entities(T)/attribute_cues(T)/triggers(T) , relations(R), events(E) or attributes(A)


### json-format data
Each encodes an instance with a format of :

```json
{
    "id": (str) sample id, 
    "context": (str) sentence text, 
    "is_multi_event": (bool), if the case belongs to the mult_event subset. Note that sub-event (Combination) is also considered as an event here, which means that a case with an ADE/PTE and a Combination subevent is labelled as multi_event as well. For cases with duplicated annotation, they are labelled as multi_event as long as either annotator annotated them with multiple events. 
    "annotations":[
        {"events": [
            {
                "event_id": (str) event id,
                "event_type": (str) event type, 
                "Trigger": {
                    // Note: for each entity, a tuple is maintained in case the span has multiple discontinuous parts.
                    // Usually, the length of each tuple is no more than 2.
                    "text": [[(str) trigger text for fragment_1, (str) trigger text for fragment_2, ...] for each entity], 
                    "start":[[(int) start position for fragment_1, (int) start position for fragment_2, ...] for each entity],
                    "entity_id": [(int) entity_id for each entity],
                    },
                "Subject":{
                    "text": [[(str) subject text for fragment_1, (str) subject text for fragment_2, ...] for each entity],
                    "start": [[(int) start position for fragment_1, (int) start position for fragment_2, ...] for each entity],
                    "entity_id": [(int) entity_id for each entity],
                    "Age":{
                        "text": [[(str) Sub.Age text for fragment_1, (str) subject text for fragment_2, ...] for each entity],
                        "start": [[(int) start position for fragment_1, (int) start position for fragment_2, ...] for each entity],
                        "entity_id": [(int) entity_id for each entity],
                    },
                    "Gender": structured as Subject.Age,
                    "Population": structured as Subject.Age,
                    "Race": structured as Subject.Age,
                    "Disorder": structured as Subject.Age,
                }
                ,
                "Treatment": {
                    "text": [[(str) Treatment text for fragment_1, (str) Treatment text for fragment_2, ...] for each entity],
                    "start": [[(int) start position for fragment_1, (int) start position for fragment_2, ...] for each entity],
                    "entity_id": [(int) entity_id for each entity],
                    "Drug": structured as Subject.Age,
                    "Dosage": structured as Subject.Age,
                    "Freq": structured as Subject.Age,
                    "Route": structured as Subject.Age,
                    "Time_elapsed": structured as Subject.Age, 
                    "Disorder": structured as Subject.Age, 
                    "Combination": [{ //sub-event
                        "event_id": (str) event id,
                        "event_type": (str) event type, 
                        "Trigger": structed as trigger,
                        "Drug": structured as Subject.Age,
                    } for each Combination]
                },
                "Effect":{
                    "text": [[(str) effect text for fragment_1, (str) effect text for fragment_2, ...] for each entity],
                    "start": [[(int) start position for fragment_1, (int) start position for fragment_2, ...] for each entity],
                    "entity_id": [(int) entity_id for each entity],
                },
                "Speculation": {
                    "text": [[(str) speculation cue text for fragment_1, (str) speculation cue for fragment_2, ...] for each entity],
                    "start": [[(int) start position for fragment_1, (int) start position for fragment_2, ...] for each entity],
                    "entity_id": [(int) entity_id for each entity],
                    "value": true/false (by default false),
                },
                "Negation":{
                    "text": [[(str) negation cue text for fragment_1, (str) negation cue text for fragment_2, ...] for each entity],
                    "start": [[(int) start position for fragment_1, (int) start position for fragment_2, ...] for each entity],
                    "entity_id": [(int) entity_id for each entity],
                    "value": true/false (by default false),
                },
                "Severity":{
                    "text": [[(str) severity cue text for fragment_1, (str) severity cue text for fragment_2, ...] for each entity],
                    "start": [[(int) start position for fragment_1, (int) start position for fragment_2, ...] for each entity],
                    "entity_id": [(int) entity_id for each entity],
                    "value": (str) High/Medium/Low (by default Medium), 
                }
            } for each event in the sentence]
        }
    for each annotator's annotation if has duplicated annotation]
    
}
```