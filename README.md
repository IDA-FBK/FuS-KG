[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa] [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/IDA-FBK/FuS-KG/tree/main/notebook) [![HTML Documentation](https://img.shields.io/badge/Widoco-Documentation-blue)](https://ida-fbk.github.io/FuS-KG/documentation/html-docs/index.html)


[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg

# FuS-KG: A Multi-Modal Knowledge Graph Supporting Personalized Health

Functional Status Information (FSI) describes physical and mental wellness
at the whole-person level. It includes information on activity performance, social
role participation, and environmental and personal factors affecting a person’s
well-being and quality of life. Collecting, integrating, and analyzing this multi-
modal information spanning different domains is crucial for addressing the needs
of an aging global population and providing effective care for individuals with
chronic conditions, multi-morbidity, and disabilities. Multi-Modal Knowledge
Graphs represent a suitable way for integrating this information in a complete and
structured way, allowing for reasoning and building tailored coaching solutions
that support individuals in their daily lives for healthy living. **FuS-KG** aims to play a central role concerning the design and development of
middle-layer applications of explainable behavior change systems allowing: (i) modeling
conceptual information representing individuals’ FSI and the use of the information to
adapt the generation of explanatory and motivational messages to the individual; (ii)
supporting interoperability among different systems which could share, for example,
databases of motivational messages or explainability algorithms; and, (iii) managing
privacy and ethical issues relating to user data.

## Building Pipeline
<br>
<div align="center"> <img src="./diagrams/pipeline/fuskg-building_pipeline.png" alt="FuSKG Building Pipeline"> </div>
<br><br>

The building pipeline of the FuS-KG is divided into 4 blocks:
### 1. **Context Analysis**

The first block of the pipeline is the context analysis, which primarily involves a comprehensive review of the literature about resources on FSI. The outcome of this analysis is the formulation of the following research questions (RQ<sub>s</sub>):

- **RQ<sub>1</sub>**: Which is the set of conceptual domains covering the entire knowledge required to represent completely and effectively the FSI of a user, and how such domains can be integrated with the dynamicity of user-generated knowledge?  
- **RQ<sub>2</sub>**: : How the whole elicited knowledge representing all the FSI domains should be structured to be reused by different solutions having different goals?  
- **RQ<sub>3</sub>**: Which is a suitable methodology to build and maintain a highly complex and huge size KG integrating knowledge representing complementary domains?  

These questions guide our investigation into how FSI can be managed, integrated, and utilized within FuS-KG.

### 2. **Co-design Activities:** 

This phase is crucial for identifying a comprehensive set of requirements (REQ<sub>s</sub>) that FuS-KG has to satisfy. Each requirement
is further decomposed into a list of competency questions (CQ<sub>s</sub>) to refine the scope of
FuS-KG.

- **REQ<sub>1</sub>**: Conceptualize food domain at a granular level (nutrients to complex recipes).
- **REQ<sub>2</sub>**: Provide activities with effort metrics to determine food requirements.
- **REQ<sub>3</sub>**: Model barriers affecting activities, food intake, and adherence to guidelines.
- **REQ<sub>4</sub>**: Include images, videos, and other modalities to support education and knowledge injection.
- **REQ<sub>5</sub>**: Define a user model and link it to domain knowledge while meeting privacy and data requirements.
- **REQ<sub>6</sub>**: Define guidelines for behavior intervention.
- **REQ<sub>7</sub>**: Incorporate time aspects for activity steps, guideline adherence, and data tracking.
- **REQ<sub>8</sub>**: Use modular design for scalability and ease of maintenance.

> [!NOTE]  
> - The detailed description of each REQ together with the list of associated CQ<sub>s</sub> is accessible at [FUSKG-REQs&CQs](/requirements).

### 3. **Modularization**
<div align="center"> <img src="./diagrams/fuskg-modules/fuskg-modules.png" alt="FuSKG Modules"> </div>
<br>

The third block focuses on the modularization of the knowledge. In
this phase, the knowledge about different domains is divided into distinct “knowledge
modules”. Each module encapsulates information related to a specific domain, such
as user, activities, and food. This modular approach facilitates easier management and
scalability of the knowledge base. Furthermore, by adopting a domain-specific split,
we ensure that each module can be developed and updated independently, promoting
modularity and reusability. To achieve this, the modularization followed the principles of the Modular ontology modeling (MOMo) methodology.
<br>

- **CORE:** [[DIAGRAM]](/diagrams/core/core_module.png) [[TBOX]](/ontology/TBox/fuskg-core.ttl) [[HTML-DOC]](https://ida-fbk.github.io/FuS-KG/documentation/html-docs/modules/Core/index-en.html)
- **FOOD:** [[DIAGRAM]](/diagrams/food/food_module.png) [[TBOX]](/ontology/TBox/fuskg-food.ttl) [[HTML-DOC]](https://ida-fbk.github.io/FuS-KG/documentation/html-docs/modules/Food/index-en.html)
- **ACTIVITY:** [[DIAGRAM]](/diagrams/activity/activity_module.png) [[TBOX]](/ontology/TBox/fuskg-activity.ttl) [[HTML-DOC]](https://ida-fbk.github.io/FuS-KG/documentation/html-docs/modules/Activity/index-en.html)
- **BARRIER:** [[DIAGRAM]](/diagrams/barrier/barrier_module.png) [[TBOX]](/ontology/TBox/fuskg-barriers.ttl) [[HTML-DOC]](https://ida-fbk.github.io/FuS-KG/documentation/html-docs/modules/Barriers/index-en.html)
- **DISEASE:** [[DIAGRAM]](/diagrams/disease/disease_module.png) [[TBOX]](/ontology/TBox/fuskg-disease.ttl) [[HTML-DOC]](https://ida-fbk.github.io/FuS-KG/documentation/html-docs/modules/Disease/index-en.html)
- **RECIPES:** [[DIAGRAM]](/diagrams/recipes/recipes_module.png) [[TBOX]](/ontology/TBox/fuskg-recipes.ttl) [[HTML-DOC]](https://ida-fbk.github.io/FuS-KG/documentation/html-docs/modules/Recipes/index-en.html)
- **MULTI-MODAL:** [[DIAGRAM]](/diagrams/multi-modal/multi-modal_module.png) [[TBOX]](/ontology/TBox/fuskg-multimodal.ttl) [[HTML-DOC]](https://ida-fbk.github.io/FuS-KG/documentation/html-docs/modules/Multimodal/index-en.html)
- **TEMPORAL:** [[DIAGRAM]](/diagrams/temporal/temporal_module.png) [[TBOX]](/ontology/TBox/fuskg-temporal.ttl) [[HTML-DOC]](https://ida-fbk.github.io/FuS-KG/documentation/html-docs/modules/Temporal/index-en.html)
- **GUIDELINES:** [[DIAGRAM]](/diagrams/guidelines/guidelines_module.png) [[TBOX]](/ontology/TBox/fuskg-guidelines.ttl) [[HTML-DOC]](https://ida-fbk.github.io/FuS-KG/documentation/html-docs/modules/Guidelines/index-en.html)
- **USER:** [[DIAGRAM]](/diagrams/user/user_module.png) [[TBOX]](/ontology/TBox/fuskg-user.ttl) [[HTML-DOC]](https://ida-fbk.github.io/FuS-KG/documentation/html-docs/modules/User/index-en.html)

> [!NOTE]  
> For more information, please refer to Section 5 of the paper, the [README.md](https://github.com/IDA-FBK/FuS-KG/blob/update-modules/diagrams/README.md) in the diagrams folders, and the available [HTML-DOCS](https://ida-fbk.github.io/FuS-KG/documentation/html-docs/index.html)

### 4. **Ontology Construction:** 

The final block involves the construction of the ontology.
This phase follows the METHONTOLOGY methodology, which provides a structural
approach to ontology development. During this
phase, the conceptual model of FuS-KG is developed, incorporating the requirements
and competency questions identified in the co-design activities block. The ontology construction
ensures that FuS-KG has a robust and flexible conceptual framework capable
of integrating and managing FSI.

> [!NOTE]  
> - For more information, please also refer to Section 6 of the paper.
> - All the ABox are available at: [[FusKG-Abox]](/ontology/ABox/).
> - Two Turtle files showing how to model user’s health data within FuS-KG and the sequence of steps required to complete an activity (not cooking domain) with a corresponding resource available online, are available [here](/example/) (also used in the notebook).

## 🚀 Google Colab Notebook

We have implemented a Python **Colab Notebook** showing how to interact with FuS-KG modules by performing SPARQL queries based on the CQ<sub>s</sub> of each REQ ([FUSKG-REQs&CQs](/requirements)). 

Click below to access the interactive notebook:

<a href="https://github.com/IDA-FBK/FuS-KG/tree/main/notebook" style="text-decoration: none;">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab">
</a>

<p></p>

> **⚠️ Important**
> 
> To load and run the notebook correctly, please follow the instructions in the [README.md](https://github.com/IDA-FBK/FuS-KG/blob/main/notebook/README.md).

## Authors
- Tania Bailoni: tbailoni@fbk.eu
- Gianluca Apriceno: apriceno@fbk.eu
- Mauro Dragoni: dragoni@fbk.eu

## License
This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
