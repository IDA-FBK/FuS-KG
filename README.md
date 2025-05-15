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

<br>
<div align="center"> <img src="/diagrams/pipeline/fuskg-building_pipeline.png" alt="FuSKG Building Pipeline"> </div>
<br><br>

## Ontology development

We developed FuS-KG by combining **METHONTOLOGY** and **Modular Ontology Modeling (MOMo)** methodologies, ensuring a systematic and modular lifecycle for building, maintaining, and evolving the knowledge graph. The process included:

1. **Specification**
    
   Starting from research questions (RQs):
    
    - **RQ<sub>1</sub>**: Which is the set of conceptual domains covering the entire knowledge required to represent completely and effectively the FSI of a user, and how such domains can be integrated with the dynamicity of user-generated knowledge?  
    - **RQ<sub>2</sub>**: How the whole elicited knowledge representing all the FSI domains should be structured to be reused by different solutions having different goals?  
    - **RQ<sub>3</sub>**: Which is a suitable methodology to build and maintain a highly complex and huge size KG integrating knowledge representing complementary domains?  

   and a literature review on FSI and related domains, we derived a set of high-level requirements (REQs) to guide the FuS-KG development: 

    - **REQ<sub>1</sub>**: Conceptualize food domain at a granular level (nutrients to complex recipes).
    - **REQ<sub>2</sub>**: Provide activities with effort metrics to determine food requirements.
    - **REQ<sub>3</sub>**: Model barriers affecting activities, food intake, and adherence to guidelines.
    - **REQ<sub>4</sub>**: Include images, videos, and other modalities to support education and knowledge injection.
    - **REQ<sub>5</sub>**: Define a user model and link it to domain knowledge while meeting privacy and data requirements.
    - **REQ<sub>6</sub>**: Define guidelines for behavior intervention.
    - **REQ<sub>7</sub>**: Incorporate time aspects for activity steps, guideline adherence, and data tracking.
    - **REQ<sub>8</sub>**: Use modular design for scalability and ease of maintenance.

    each requirement is supported by a set of competency questions (CQs), which are fully detailed in the [FUSKG-REQs&CQs](/requirements) file available in the repository.

2. **Knowledge Acquisition**

   The acquisition of the knowledge necessary for building FuS-KG has been done in two step (i) collaborating with domain experts to model core entities (abstract classes and properties), starting from the HeLiS ontology to address key requirements; and (ii) identifying and analyzing unstructured and structured sources to populate FuS-KG.

   Data sources included:
  
    - **Food domain:** HeLiS-based models from Italian agricultural and epidemiological archives, plus four additional datasets: the USDA database, Recipe1M+, Tasty, and RecipeDB.
    - **Activity domain:** The Compendium of Physical Activities, providing a taxonomy and effort measures.
    - **Barrier domain:** The Supported Intensity Scale (SIS) manual, modeling barriers affecting a person’s functional status.
  
    From these sources, the modeling team extended the conceptual model by defining concepts and properties to cover the temporal and multi-modal information of FuS-KG.
   
    > **Note:** The links to download the raw versions of each source can be found at this [LINK](https://github.com/IDA-FBK/FuS-KG/tree/main/documentation/datasets/Source-Links).
    
4. **Conceptualization**
    
   FuS-KG’s conceptualization involved two steps: first, gathering and refining terminology from the HeLiS ontology and unstructured sources; second, refining the conceptual model and selecting ontology design patterns (ODPs). Adopted patterns from the [ODP catalog](http://ontologydesignpatterns.org/index.php/Ontology_Design_Patterns_._org_(ODP)) include logical ones like Tree and N-Ary Relation, alignment via Class Equivalence, and content patterns such as Parameter, Time Interval,        Action, and Classification.

5. **Integration**
     
     FuS-KG aligns its core concepts with the DOLCE foundational ontology and integrates external vocabularies to enhance interoperability. These include the Time Ontology (ProperInterval), DCAT (Resource), and AGROVOC for nutritional concepts, enabling linkage with the Linked Open Data (LOD) cloud. We also manually aligned FuS-KG modules with domain ontologies using Protégé. The table        below summarizes the number of matches found per module and target ontology.

     <div align="center">
        <table>
          <thead>
            <tr>
              <th><strong>FuS-KG Module</strong></th>
              <th><strong>Target Ontology</strong></th>
              <th><strong>#Matches</strong></th>
            </tr>
          </thead>
          <tbody>
            <tr><td>Food</td><td>FoodOn</td><td>131</td></tr>
            <tr><td></td><td>OntoFood</td><td>55</td></tr>
            <tr><td>Recipe</td><td>RecipeKG</td><td>5</td></tr>
            <tr><td>Activities</td><td>OPTImAL</td><td>2</td></tr>
            <tr><td></td><td>PACO</td><td>6</td></tr>
            <tr><td>Disease</td><td>HPO</td><td>56</td></tr>
            <tr><td>User</td><td>SOHO</td><td>0</td></tr>
            <tr><td></td><td>FOAF</td><td>1</td></tr>
          </tbody>
        </table>
      </div>


6. **Implementation**
   
   FuS-KG is fully represented in Turtle (TTL) format. To manage its size and promote knowledge reuse, we applied the MOMo methodology. MOMo offers flexible guidelines through a sequence of steps to define modular ontologies, allowing engineers to create domain-specific modules as needed.

7. **Evaluation**
    
   FuS-KG was thoroughly analyzed using the [OOPS! pitfall scanner](https://oops.linkeddata.es/) to identify potential issues. Most pitfalls detected related to reused ontologies (e.g., HeLiS) and included unconnected elements, missing annotations, and undeclared inverse relationships. All issues in newly developed modules were resolved.
   Consistency checks with Pellet and HermiT reasoners found no errors. Each module was individually evaluated to ensure quality, and the full FuS-KG passed successfully, confirming it is consistent, error-free, and meets all requirements.

8. **Documentation**
    
   To facilitate community access and reuse, we provide comprehensive [HTML-DOCS](https://ida-fbk.github.io/FuS-KG/documentation/html-docs/index.html) of the FuS-KG ontology, generated using the [Widoco documentation tool](https://github.com/dgarijo/Widoco).

## **Inside FuS-KG**
<div align="center"> <img src="./diagrams/fuskg-modules/fuskg-modules.png" alt="FuSKG Modules"> </div>
<br>

The knowledge about different domains of FuS-KG is divided into distinct “knowledge
modules”. Each module encapsulates information related to a specific domain, such
as user, activities, and food. This modular approach facilitates easier management and
scalability of the knowledge base. Furthermore, by adopting a domain-specific split,
we ensure that each module can be developed and updated independently, promoting
modularity and reusability. To achieve this, the modularization followed the principles of the MOMo methodology.
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
> For more information, please refer to the paper, the [README.md](https://github.com/IDA-FBK/FuS-KG/blob/update-modules/diagrams/README.md) in the diagrams folders, and the available [HTML-DOCS](https://ida-fbk.github.io/FuS-KG/documentation/html-docs/index.html)

## MMKG Construction & Materialization

**Unstructured sources preprocessing**

We cleaned recipe preparation steps from unstructured multi-modal sources by removing steps shorter than eight characters (e.g., “Easy”, “YUM!”), reducing steps from 441,911 to 429,811. After filtering duplicates across datasets (e.g., oven preheating instructions), the total steps further decreased to 364,735. Multi-modal data (images from Recipe1M+, videos from Tasty) were centralized in a [shared drive](https://fbk.sharepoint.com/:f:/s/IDA/Es_HSPcBMs5LqKT4aDSU0O4BM_BIn_yhO0kcwWVanPBVYA?e=FWfkDR) for easy access. RecipeDB was also manually integrated to enhance coverage and diversity of the overall knowledge base.

**Structured sources preprocessing**

The USDA database, originally in Excel, was manually reformatted for compatibility with Protégé. A similar process was applied to physical activity data from the Compendium of Physical Activity, initially in PDF format.

**MMKG materialization**

Using Python scripts with the `rdflib` library ([CODE](https://github.com/IDA-FBK/FuS-KG/tree/main/code)), we parsed TBox concepts and properties and linked entities from all sources (ingredients, nutrition, preparation steps, images, videos). The resulting ABox TTL files and generation scripts are available in the repository. Manual inspections ensured data integrity before publishing. The table below shows the KG metrics by module.

<div align="center">

  <table>
    <thead>
      <tr>
        <th>MODULE</th>
        <th>#Axioms</th>
        <th>#Classes</th>
        <th>#Object Properties</th>
        <th>#Data Properties</th>
        <th>#Individuals</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>CORE</td><td>80</td><td>4</td><td>4</td><td>0</td><td>0</td></tr>
      <tr><td>FOOD</td><td>1,573,179</td><td>251</td><td>1</td><td>6</td><td>140,928</td></tr>
      <tr><td>RECIPES</td><td>110,644</td><td>14</td><td>2</td><td>1</td><td>55,257</td></tr>
      <tr><td>DISEASE</td><td>27,519</td><td>3</td><td>2</td><td>1</td><td>6,095</td></tr>
      <tr><td>ACTIVITY</td><td>10,155</td><td>24</td><td>2</td><td>2</td><td>1,229</td></tr>
      <tr><td>BARRIER</td><td>2,853</td><td>40</td><td>15</td><td>11</td><td>139</td></tr>
      <tr><td>MULTI-MODAL</td><td>4,123,598</td><td>10</td><td>2</td><td>5</td><td>768,251</td></tr>
      <tr><td>TEMPORAL</td><td>4,056,607</td><td>10</td><td>4</td><td>5</td><td>1,524,016</td></tr>
      <tr><td>GUIDELINES</td><td>86</td><td>2</td><td>2</td><td>1</td><td>0</td></tr>
      <tr><td>USER</td><td>309</td><td>14</td><td>11</td><td>20</td><td>0</td></tr>
    </tbody>
  </table>

</div>


**MMKG access**  
All FuS-KG materials—including [[FusKG-Abox]](/ontology/TBox/), [[FusKG-Abox]](/ontology/ABox/), and [documentation](https://ida-fbk.github.io/FuS-KG/documentation/html-docs/index.html) are hosted on GitHub. Additionally, a [Google Colab notebook](https://github.com/IDA-FBK/FuS-KG/tree/main/notebook) enables interactive SPARQL queries based on CQs associated with the requirements REQs.

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

---
> [!NOTE]  
> - For more detailed information, please refer to the paper.
> - Two Turtle files showing how to model user’s health data within FuS-KG and the sequence of steps required to complete an activity (not cooking domain) with a corresponding resource available online, are available [here](/example/) (also used in the notebook).

## Authors
- Tania Bailoni: tbailoni@fbk.eu
- Gianluca Apriceno: apriceno@fbk.eu
- Mauro Dragoni: dragoni@fbk.eu

## License
This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png

