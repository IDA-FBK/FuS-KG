# Examples: User and NotCooking Activity

This folder contains two Turtle files that represent two examples showing how to model:
- User’s health data inside FuS-KG (e.g., individual’s food consumption and activity logs) . This is useful since FuS-KG can be exploited for health monitoring, analysis, and personalized recommendations.
- The sequence of steps required to complete an activity (not cooking domain) with a corresponding resource available online. This is particularly useful for instructional applications, where a user may follow a series of steps to perform a task, and multimodal resources provide additional guidance. 

## Overview of the Files

### 1. **fuskg-user-example.ttl**

This file is an example of a user’s health data, including the individual’s food consumption, activity logs, and related health data. The key elements in this file are:

- **User Information**: Represents an individual user (`PatientX`) and its interactions with food and activities.
- **Food Consumption**: Documents consumed food items (`:Breakfast-PX-1`, `:Dinner-PX-5`, etc.) and their quantities using the USDA food database.
- **Activities**: Logs activities performed by the user (`ACT-PX-1`, `ACT-PX-2`), including activity start time, duration, and end time.
- **Disease Risk**: Links food items and activities with disease risks (e.g., `DRL-USDAFOOD-00001-C` for a cardiovascular risk level).
- **Monitoring Rules**: Defines rules to monitor specific behaviors, such as food intake and physical activity (`MR1-PX`, `MR2-PX`, etc.).
- **Relationships**: Includes how diseases are related to the user and how barriers, such as chest pain or the cost of a bike, impact performing activities.

### 2. **fuskg-notcooking-example.ttl**

This file is an example of an activity (i.e., remove lampashade - not cooking domain) with a corresponding resource avaible online . The key elements in this file are:

- **Activity and Step Descriptions**: Represents a series of activity steps required to complete a task. For example, the activity `ACTIVITY-05160-B` includes steps like `ActivityStep-ACTIVITY-05160-B-1`, `ActivityStep-ACTIVITY-05160-B-2`, etc., each of which is temporally ordered and described with specific instructions (e.g., "Remove the lampshade").
- **Temporal Sequencing**: Defines how steps in an activity are temporally linked using properties like `fstemp:afterStep` and `fstemp:beforeStep`. These properties ensure that steps follow a specific order, and also specify when each step begins and ends with `fstemp:orderedStepBegin` and `fstemp:orderedStepEnd`.
- **Steps Descriptions**: Each step is linked with a description of what needs to be done at that particular stage (e.g., "Take out the old bulb").
- **Modal Descriptor**: The multimodal descriptor (`fsmumo:hasModalDescriptor`) links the activity to an online video resource, which is associated with a specific modality (with specific metadata info, e.g., width, height and fps), to support the activity.


> **Interact with those files in the Notebook:**
> 
><a href="https://github.com/IDA-FBK/FuS-KG/tree/main/notebook" style="text-decoration: none;">
>  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab">
></a>

