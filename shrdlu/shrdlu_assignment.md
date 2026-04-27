# Assignment: From SHRDLU to Modern Grounded NLP

## Overview

In this assignment, you will start from the simplified SHRDLU-style blocks world in this chapter and progressively redesign it into a richer natural language understanding system. The goal is to connect classic symbolic NLP ideas with modern statistical and neural methods.

You will build a system that interprets commands about a small world, resolves references to objects, and updates a world model after each action. The assignment is organized in three stages:

1. Rule-based parsing and symbolic world representation
2. Classical and sequence models for intent and slot prediction
3. Hugging Face open-source models for richer language understanding and more diverse world representations

The final system should go beyond the original blocks world and support a more varied environment such as rooms, containers, furniture, tools, animals, vehicles, or mixed everyday objects.

## Background

The original SHRDLU system worked in a constrained microworld. Its strength came from combining:

- a formal representation of the world
- a language parser
- reference resolution
- action planning

Your task is to reproduce that basic pipeline first, then improve it using classical machine learning models, sequence models, and transformer-based open-source models.

You may use the material in the following files as your starting point:

- shrdlu.ipynb
- shrdluGradio.ipynb

## Learning Objectives

By completing this assignment, you should be able to:

- design a symbolic world representation for grounded language tasks
- implement a basic parser for commands and references
- model intent detection and slot filling using classical and sequence learning methods
- compare symbolic, statistical, and transformer-based approaches
- evaluate robustness, ambiguity handling, and generalization
- justify architectural design choices with experiments

-----
-----

## Task Summary

Build an interactive grounded language system that can:

- represent a world with at least 12 distinct objects
- support at least 4 object attributes such as color, size, shape, type, material, state, or location
- process at least 5 action types such as pick up, move, place, open, close, inspect, push, or give
- handle ambiguous references by asking for clarification or ranking candidates
- maintain and update world state after each command
- explain or display the action sequence used to execute the request

## Project Path Options

You may complete the assignment in one of the following two ways.

### Option 1: SHRDLU-Inspired New World

Use SHRDLU as the conceptual starting point, but design your own world representation from scratch. You should keep the core ideas of parsing, grounding, reference resolution, and action execution, while building a richer domain of your own.

Examples include:

- a kitchen assistant world
- a smart room environment
- a warehouse robot world
- an office or desktop assistant world

This option is more demanding because it requires you to design both the world model and the language interface around it.

**Award note:** The top 5 students who choose Option 1 and deliver a substantially different, coherent, and well-executed world representation will receive special recognition for this assignment.

### Option 2: Extend the Existing SHRDLU System

Start from the current SHRDLU-style notebook and directly expand the existing system. In this version, you keep the original blocks-world foundation but make it richer by adding more object types, more relations, more language variation, and stronger learning-based components.

Examples of valid extensions include:

- more block attributes and relations
- support for containers or zones within the world
- more complex multi-step commands
- improved ambiguity handling
- learned parsing and transformer-based interpretation on top of the existing system

This option is more constrained, but it gives you a clearer implementation starting point.
----
---

## Required Progression

You must complete the project in the following three stages.

## Stage 1: Symbolic SHRDLU Baseline

Implement a rule-based baseline inspired by the current notebook.

### Minimum Requirements

- define a structured world model using Python classes or dataclasses
- represent object attributes and relations explicitly
- implement a small rule-based parser for commands
- support reference resolution such as:
  - "pick up the red cube"
  - "move the small green box onto the wooden table"
  - "put the object next to the chair inside the container"
- implement simple planning or ordered action execution
- handle failure cases with meaningful error messages

### Suggested Design

Your pipeline can follow this structure:

1. Parse utterance into intent and arguments
2. Resolve arguments against world entities
3. Check preconditions
4. Generate action plan
5. Execute plan and update world state

### Example: Symbolic Baseline

For a command such as `pick up the red cube`, a Stage 1 symbolic system might:

1. parse the command as `intent = PICKUP`
2. resolve `red cube` against the objects in the world
3. check whether that object is clear and can be picked up
4. generate a simple action such as `pickup(b1)`
5. update the world state to show that the agent is now holding that object

This example is intentionally simple. The main goal of Stage 1 is to show that the symbolic pipeline is explicit, interpretable, and grounded in the world representation.

### Deliverable for Stage 1

- working symbolic system
- brief explanation of grammar rules and world assumptions
- at least 10 example commands with outputs

## Stage 2: Classical and Sequence Models

Replace part of the hand-written language pipeline with learned models.

### Goal

Use learned models to predict linguistic structure from text. You may choose one of the following directions, or combine them:

- intent classification
- slot filling or token labeling
- action sequence prediction from commands
- reference extraction from natural language descriptions

Classical classifiers are most suitable for tasks such as intent classification or command type prediction, while sequence models are more suitable for token labeling and structured parsing.

### Example: Intent Classification vs Sequence Labeling

For a command such as `put the red cube on the blue box`, students may model Stage 2 in different ways:

- as an intent classification task, where the full command is assigned a label such as `PUT_ON`
- as a sequence labeling task, where each token is labeled, for example `put -> ACTION`, `red -> COLOR`, `cube -> OBJECT`, `on -> RELATION`, `blue -> COLOR`, `box -> OBJECT`

Either approach is acceptable, and students may also combine both if that better supports their system.

### Model Options

You may implement one or more of the following:

- Naive Bayes
- logistic regression
- SVM
- Hidden Markov Model
- RNN
- LSTM 
- encoder-based sequence tagger
- ... or any other Classical or Sequence Model you find suitable

### Minimum Requirements

- create or curate a small labeled dataset of commands
- define labels clearly, for example `B-COLOR`, `B-OBJECT`, `B-LOCATION`, `INTENT_MOVE`
- train at least one learned model
- compare it against the symbolic baseline on a clearly defined subtask
- report where the model helps and where it fails

### Evaluation Suggestions

Measure some of the following:

- intent accuracy
- token-level precision, recall, and F1
- exact match for parsed command structure
- success rate of full world execution

### Deliverable for Stage 2

- training data description
- model implementation and training results
- comparison table between rule-based, classical, and sequence-model approaches where relevant

## Stage 3: Hugging Face Open-Source Models

Extend the system using an open-source model from Hugging Face.

### Goal

Use a pretrained model to make the system more flexible, more robust to varied phrasing, and capable of operating over a more diverse world representation.

### Minimum Requirements

- use at least one open-source Hugging Face model
- document why you selected it
- integrate the model into the command understanding pipeline
- expand the world beyond the original blocks setting
- demonstrate improved handling of linguistic variation

### Suitable Model Families

You may use lightweight open-source models such as:

- DistilBERT or BERT for intent classification or token classification
- T5 or FLAN-T5 for structured command normalization
- sentence-transformers models for semantic matching and reference resolution
- small instruction-tuned open models for command rewriting into a structured schema

### Example Extensions

- allow paraphrases such as "place the blue object over the red one"
- support indirect references such as "the thing near the window"
- support stateful descriptions such as "the open box" or "the broken tool"
- support mixed object domains such as kitchen, office, or robot navigation worlds

### Important Constraint

Do not use closed commercial APIs. Use open-source models that are accessible through Hugging Face.

### Deliverable for Stage 3

- description of chosen model and integration method
- examples showing improved generalization
- error analysis comparing Stage 2 and Stage 3

## World Representation Requirement

Your final system must use a richer world representation than the original notebook.

### Minimum World Complexity

- at least 12 objects
- at least 3 relation types such as `on`, `inside`, `next_to`, `under`, `holding`, `near`
- at least 4 attribute types
- at least 2 locations or zones if appropriate
- at least 1 source of ambiguity that your system can detect and handle

### Example Domains

Choose one domain or design your own:

- smart room assistant
- kitchen robot assistant
- warehouse manipulation world
- office desktop environment
- game inventory and room navigation world

## Implementation Expectations

Your submission should include:

- Python code or notebooks
- one short report in Markdown or PDF
- reproducible instructions to run the system
- sample inputs and outputs
- experiments and evaluation results

You may build a notebook-based demo or a small interface similar to the Gradio example.

## Suggested Repository Structure

```text
project/
  data/
  notebooks/
  models/
  src/
    world.py
    parser.py
    planner.py
    train_sequence_model.py
    hf_pipeline.py
  report.md
```

## Experiments and Analysis

Your report should answer the following questions:

1. What worked well in the symbolic baseline?
2. What kinds of language broke the rule-based parser?
3. Did the sequence model improve robustness? On which tasks?
4. What extra capability did the Hugging Face model provide?
5. What errors still remain in the final system?
6. How does world representation affect interpretation quality?

## Deliverables

Submit the following:

1. Source code or notebook implementation
2. A short report of 4 to 6 pages
3. A demo file or script with example interactions
4. A results section with quantitative and qualitative evaluation

## Technical Documentation Structure

The technical documentation or report should be structured clearly and should include the following sections:

1. Introduction
2. Related Work or Background
3. Methodology for all Stages
4. Application or Implementation of the Methodology
5. Discussion of Results

Students may include additional sections if useful, but the report should make the progression across the three stages easy to follow.

## Marking Scheme

| Component | Weight |
|---|---:|
| Stage 1: symbolic baseline | 25% |
| Stage 2: sequence model design and evaluation | 25% |
| Stage 3: Hugging Face integration and richer world model | 25% |
| Report quality and analysis | 15% |
| Code quality, clarity, and reproducibility | 10% |

## Assessment Criteria

High-quality submissions will:

- show a clear progression from symbolic to learned methods
- define the world representation carefully
- evaluate with concrete examples and metrics
- discuss failure cases honestly
- make technically sound use of Hugging Face models rather than adding them superficially


## Optional Extensions

You may explore one or more of the following:

- dialogue context across multiple turns
- visual grounding with images or diagrams
- automatic world generation
- multilingual commands

## Notes on Tools and Models

Students may use standard NLP and ML libraries such as `scikit-learn`, `NLTK`, `spaCy`, `PyTorch`, `TensorFlow`, `Transformers`, and similar open-source tools. These libraries are allowed to support the project, but they should not replace the core requirements of the assignment.

### Stage-Specific Expectations

- In Stage 1, the core symbolic pipeline should be student-built. You may use small utility libraries, but not a black-box parser, POS tagger, or end-to-end pretrained system as the main solution.
- In Stage 2, students must train at least one learned model themselves.
- In Stage 3, pretrained open-source models are explicitly allowed and encouraged, provided they are integrated thoughtfully and evaluated properly.

### POS Tagging and Pretrained Models

- Students may use library-based POS tagging or other pretrained NLP components as supporting tools.
- However, these should not be submitted as the main learned contribution for Stage 2.
- If a pretrained POS tagger or classifier is used, students must explain why it was used, what role it plays, and what part of the system is still their own contribution.

### Required Learned Model Constraint

At least one student-trained learned model must be included in the project and should perform reasonably well on a clearly defined constrained task.

Examples of acceptable constrained tasks include:

- intent classification over a fixed command set
- slot filling for a limited domain vocabulary
- reference classification among a small set of candidate objects
- action prediction in a restricted microworld

Students should define the constrained task clearly, report evaluation results, and explain the limits of that model beyond the constrained setting.

## Academic Integrity

- you may use open-source libraries and pretrained models with proper citation
- if you use generated data, describe exactly how it was created
- if you use AI assistants for coding support, document that usage and ensure the final code is your own work
- all submitted analysis and design decisions must be your own work

## Submission Checklist

- symbolic baseline implemented
- sequence model trained and evaluated
- Hugging Face model integrated
- richer world representation completed
- report included
- instructions to run included
- examples and error analysis included

## Suggested Starting Point

Start by reusing the basic world, parser, and execution logic from the SHRDLU notebook. Once the symbolic system is stable, isolate the language understanding layer so you can swap:

- rule-based parsing in Stage 1
- sequence labeling or intent models in Stage 2
- pretrained transformer-based components in Stage 3

This separation will make your system easier to evaluate and extend.

Teams of up to 2 students are allowed. If you work in a team, please clearly indicate the contributions of each member in the report.