# Problem Decomposition for Program Synthesis with Large Language Models
----
## Introduction
- This is a project about [XJTLU](https://www.xjtlu.edu.cn/en) Surf 2023. Program synthesis generates computer programs based on given problem specifications. Large Language Models have been proven to be effective. However, models are still struggling
to handle complicated tasks involving multiple steps. Recently, a multi-turn code generation benchmark has been proposed. They provide pre-defined individual steps in natural
language. However, this setting is not very useful in practice. Instead of starting from a pre-decomposed steps, we aim to automatically decompose the a short problem specification
into individual steps. We reverse-engineered the multi-turn benchmark to include a short summary specification. We empirically examined the ability of current models to
automatically decompose the summary specification and complete the task given the decomposed steps
----
## Guidline
- Use experiment.ipynb to get the code and reward.
- As somtimes the reward may not be true,you can use testall.py and then please use classifitf.py
- Finally, use draw.py to show the accuracy.
----
## Poster
- [Download SURF 2023 Poster (PDF)](Poster_and_report/SURF-2023-0040-Poster)


![SURF 2023 Poster](Poster_and_report/SURF-2023-0040-Poster.jpg)
