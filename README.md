# Final Project

**Important Note:** This is **NOT** an Above & Beyond assignment; your basic score will be calculated out of the full 100 points.

## Synopsis

The goal of the final project is to have fun computing with photographs! You will use what you’ve learned in this class, and (hopefully) also learn something new in the process. The final project combines a bit of research and some coding to produce a novel visual artifact (image or video).

This document provides report content information, a link to the report template, and instructions for other deliverables (images and code), and FAQs.

Refer to the Final Project Description and Proposal for project requirements. That information is not duplicated here.


### Overview of deliverables

1) Project report following the template provided
2) Source code (including instructions to generate the results illustrated in your report)
3) All inputs & outputs presented in your report

Note: If the total size of your inputs/outputs exceeds 5-10MB, then you should host them online and submit a link to those resources in your report, rather than the files themselves.


## What will be evaluated?


### 1. Completion

Develop a working implementation of your project with working code, a final report, and sample input and output results. You may choose how best to showcase your results, just as long as we can see them. (e.g., if your results are best shown as a video, then record it and share that). Results may be hosted on other sites, with links shared. Input images and output results must be shown at a minimum. Intermediate steps that demonstrate your process are valuable as well.

Although your implementation does not have to fully succeed for you to pass the project, you should definitely have some results to showcase.

### 2. Example Inputs & Outputs

Show that your project works on various inputs by submitting at least three complete examples of inputs/outputs. Your results must be shown in your report, and you must provide access to the files such that TAs can reproduce your results by running your code on the submitted files.

The example images should be your own work. You may include examples from other sources (for example, to replicate previously published results), but you must also provide your own original inputs. Taking good images to support your work is an important part of the process. If your project is extremely complex and you are unable to do three examples, contact us in advance on Piazza for approval. For reference, in the past we've only made exceptions when students could only arrange one flight with an instrumented plane, or one trip on a ship to obtain video for ship detection.

### 3. Source Code

This is the center of your project. See the Final Project Description and Proposal document for specific requirements and warnings concerning code.

### 4. Pipeline

Specify a workflow or pipeline for your project and explain it in good detail. Further guidance for the pipeline is in the template. Here’s a simple example:

![](pipeline.png)

### 5. Details

Details of what was done, what worked, what didn't work, and showcasing intermediate and final results.  Give detailed descriptions and explanations. Show images from your steps, and discuss them.


## Submission Requirements

Make a copy of the [final report template](https://docs.google.com/presentation/d/1JCMQWOgD4D2Nxa6oyN4F7CNOGs515jKaGcdpqtiklk0/edit?usp=sharing).

Your submission must include the following:
- A folder or zip file containing your code file(s)
- A file named README.txt that contains basic instructions on running your code, including what libraries, languages, etc., (including versions) to use, as well as what commands to use to run your code. This doesn’t need to be extremely detailed as long as we can successfully run your code based on your instructions.
- Input images and final artifact sets.  Reduce your image sizes to fit the report limit.  Name the images so that it is clear which ones go together (i.e. set1_input.png, set1_output.png).  Your images must be one of the following types: jpg, jpeg, bmp, png, tif, or tiff. If the total size of your inputs/outputs exceeds the size limit, then you should host them online and submit a link to those resources in your report, rather than the files themselves.
- Any additional files that you wish to submit in support of your project. The total file size for ALL files must be less than the specified limit.  


## Submit the Project

Zip your report & resource files into an zip archive and submit it in Canvas for this project. The name of the zip file is not important.

**Note:** The total size of your project (report + resources) must be less than 12MB for this project. If your submission is too large, you can reduce the scale of your images or report.


## Frequently asked Questions

### What programming language / development platform is required?
- You may choose.  We are interested in seeing the input and the output. We trust that you will not fake the results, but you are required to submit your code.  

### I can’t think of what makes an appropriate final project, can you suggest one?
- Feel free to ask for ideas and suggestions on Piazza. We will provide some suggestions, but we really do want you to think about one. We suggest searching for Computational Photography Projects and look for classes on this topic at other universities. Review the technical papers included in Resources. Many of these can be recreated.

### Are we allowed to share our code with other students?
- You may NOT share code with other students before the project deadline. You may share ideas and/or outputs (i.e. image results), but make sure to cite your sources if you get ideas from elsewhere. Once the project closes, you may share your code if you choose. 

### Are we allowed to use code from other sources?
- Yes, you may use support libraries for basic functionality, but you must compose the computational pipeline (workflow) on your own. You must also acknowledge the authors of any libraries/code you use in your report. For example, our projects all use openCV for image I/O and most basic operations like filtering; and we use numpy for arithmetic & matrix/vector operations. These are all acceptable uses. In contrast, during the seam carving project it was explicitly stated that using the seam carving implementation from scikit-image was not allowed. Similar rules apply here. If your project is to write code that does X, then you should not rely on a library to do X. Feel free to ask for clarification if you are unsure.

### I have made a very cool effect to do X, can I make a short video to showcase it?
- Absolutely, we would love to see it. Make sure to also describe the details of your effect (see www.cc.gatech.edu/dvfx for examples (rather old)). 

### I have  taken on a very hard project and it seems I may not finish. What should I do?
- Reduce the scope; find some parts you can complete and get some results.  We want to see something and your attempt at it.  You do not need to get re-approval.

### I have taken on a very simple project, what can I do?
- Increase the scope; do more, apply it to harder input, to video, etc. 

### I would like to apply threshold edge detection and several filters to an image, as part of an app, is that enough?
- This is usually not enough, as filtering is extremely simple. You would need to apply additional processes involving computation for this project.

### My project is very complex, and I can’t show three examples. What do I do?
- If you have a really good reason, then we can allow you to use only one or two examples. Contact us via private Piazza post ahead of time. For example:  We had a student who arranged to put markers on an airplane wing, and then did video measurements during flight. He could only arrange for one flight. Someone else had similar issues with ship detection in limited visibility. Both of these had significant issues surrounding limited access test events.

### What is the desired outcome of this project?
- Having fun computing with photographs! 
