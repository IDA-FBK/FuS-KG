# FuS-KG Modules

FuS-KG is a Multi-Modal Knowledge Graph designed to integrate and represent knowledge about food, activities, barriers, diseases, recipes, guidelines, and user interactions.
The knowledge contained in FuS-KG is currently organized into several modules: **Core**, **Food**, **Activity**, **Barrier**, **Disease**, **Recipes**, **Multi-Modal**, **Temporal**, **Guidelines**, and **User**.

## Modules

### 1. Core Module
The **Core** module defines the foundational concepts of FuS-KG. These include:

- **Activity**: Represents different types of activities.
- **Barrier**: Represents obstacles that may affect activities or the consumption of foods and nutrients.
- **Food**: Defines foods and their nutritional properties.
- **Nutrient**: Describes the nutrients contained in foods.

Relationships between these concepts include:

- `contains`: Specifies that a particular food contains another food.
- `hasNutrient`: Defines the nutrients contained in a food.
- `affectsPerformingOf`: Connects barriers to activities that they hinder.
- `concernsConsumptionOf`: Links barriers to the consumption of specific foods or nutrients.

### 2. Food Module
The **Food** module imports the **Core** module and focuses on specific foods and their nutrients. Key concepts include:

- **BasicFood**: Foods with detailed nutritional information (e.g., White Bread).
- **ComposedFood**: Aggregations of instances of **BasicFood** (e.g., Tomato Sauce).
- **Nutrient**: Categorized nutrients such as Protein, Vitamin, and Dietary Fiber.

Nutritional properties are represented by:

- `amountNutrient` and `unit`: Nutrient amount and its unit.
- `amountCalories`, `amountEnergy`, and `amountWater`: Calories, energy (in Joules), and water content per 100 grams.
- `ediblePart`: The edible portion per 100 grams.

### 3. Activity Module
The **Activity** module imports the **Core** module and classifies activities into:

- **LifeActivity**: Activities related to daily living.
- **PhysicalActivity**: Activities involving physical exertion.

Each activity is connected to a **SpecializedActivity** based on the practitioner type (e.g., adult, older adult, wheelchair user) using the `practicedBy` property. Effort is represented by:

- `hasMETValue`: The Metabolic Equivalent of Task (MET).
- `hasUnitKCalValue`: Calories required per minute per kilogram of body weight.

### 4. Barrier Module
The **Barrier** module imports the **Core** module and include:

- **CognitiveBarrier**, **HealthBarrier**, **PsychologicalBarrier**, **PhysicalBarrier**: Categories of barriers affecting activities, foods, or nutrients.

Other key concepts include:

- **StateOfChange**: Represents the user's attitude toward behavior change (e.g., Pre-contemplation, Contemplation).
- **Patient**: Represents a user with a diagnosis connected to a **DiseaseRelation**, which models the relationship between a disease and a health barrier.

### 5. Disease Module
The **Disease** module imports the **Food** module and models food-disease relationships using the **DiseaseRiskLevel** concept. Key properties include:

- `hasFood`: Refers to the food in the relationship.
- `hasDisease`: Refers to the disease in the relationship.
- `hasRiskLevel`: Specifies the risk level of the food-disease pair.

### 6. Recipes Module
The **Recipes** module imports the **Disease** and **Food** modules. A **Recipe** is defined as a group of ingredients (specific foods) and their associated quantities. Key elements include:

- `hasRecipeFood`: Connects a **Recipe** to its ingredients (**RecipeFood**).
- `hasFoods`: Links each **RecipeFood** to a specific food (**BasicFood** or **ComposedFood**).
- `amountFood`: Specifies the quantity of each ingredient.

This module includes sub-modules for recipes collected from various sources and alignments between recipes from different sources.

### 7. Multi-Modal Module
The **Multi-Modal** module imports the **Recipes** and **Activity** modules and represents multi-modal knowledge (e.g., images and videos) associated with recipes and activities. Key concepts include:

- **ModalDescriptor**: Represents a multi-modal description.
- **ModalEntity**: Corresponds to a **Recipe** or **Activity**.
- `hasModalDescriptor`: Links a **ModalEntity** to its description.
- `hasModality`: Links a **ModalDescriptor** to its modality (e.g., image, video).

### 8. Temporal Module
The **Temporal** module imports the **Recipes** and **Activity** modules and is divided into two sub-modules:

1. **Temporal Intervals**: Define temporal intervals that may be of interest to model the guidelines (e.g, `Day` and `Meal`).
2. **Action Steps**: Represents steps required to complete actions, such as recipes or activities. Key concepts include:
   - **TemporalStep**: A step defined as a **ProperInterval** in the Time ontology.
   - `beforeStep` and `afterStep`: Define the sequence of steps.
   - `orderedStepBegin` and `orderedStepEnd`: Specify the start and end of a step.
   - `hasStepDescription`: Links a step to its description.

For recipes, **RecipeStep** is a subclass of **TemporalStep**, and the `hasFirstRecipeStep` property connects a recipe to its first step.

### 9. Guidelines Module
The **Guidelines** module imports the **Barrier** and **Temporal** modules. It models behavioral guidelines to support reasoning about recommendations. Key concepts include:

- **MonitoringRule**: Represents a rule.
- `hasRuleDefinition`: Defines the rule.
- `hasMonitoredValueInterval`: Specifies the monitored interval.
- `monitors`: Links rules to users.

### 10. User Module
The **User** module imports the **Guidelines** module, enabling the storage of user data collected through sensors, mobile applications, or other means. Key concepts include:

- **User** and **Profile**: Represent a user and their profile.
- **PerformedActivity** and **ConsumedFood**: Track activities performed and foods consumed by the user during a meal.
- **Violation**: Represents a list of a user's violations.


