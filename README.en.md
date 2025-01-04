# Random Roll Call

## Introduction
This application solves the problem of teachers' random roll call in class. It has the following advantages compared to off-the-shelf tools on the market:
1. Customizable list, with a small amount of code, making it easy to develop.
2. Built on HTML + CSS + JS at the bottom, facilitating the addition of new features.
3. Easy to run with low operating pressure.
4. A Python version is provided.
Special note: This program is compiled using HTML2EXE.

## Software Architecture
A simple application of the MVVM (Model - View - ViewModel) architecture.

## Installation Tutorial
1. Windows version: Run directly without installation or deployment. If needed, you can drag the software to the C drive and then create a shortcut on the desktop.
2. Mac version: Run directly without installation or deployment. Just click to start.
3. HTML version: 
    - Place all files in the same folder following the directory structure.
    - Prepare tools such as a browser on your local machine that can run HTML files properly.
    - Then run it.
4. Python version: Run it in an editor.

## Instructions for Use
1. Sale, modification, and distribution are prohibited without the permission of the author.
2. Appropriate modifications are allowed. However, the modified files should be clearly marked, and the original copyright notice should be retained.
3. Distribution of the software for commercial sales purposes is prohibited.

## Features
1. Customizable list, with a small amount of code, making it easy to develop.
2. Built on HTML + CSS + JS at the bottom, facilitating the addition of new features.
3. Easy to run with low operating pressure.
4. A Python version is provided.

## Special Instructions
1. Due to limitations on Gitee, special operations are required for the Mac version: Drag the files inside "build" into "build" and run them in the same system directory.
2. The development progress of the Mac version is relatively more advanced, but it has more bugs.

This is a web application for random roll call implemented with HTML, CSS, and JavaScript. The following is a detailed introduction to this project:

### Functional Overview
This web application is mainly used for random roll call among students and has the following functions:
1. **Random Roll Call**: Click the "Roll Call" button, and the program will randomly scroll and display student names from the preset student list, and finally determine an uncalled student.
2. **Color Selection**: Provide a variety of color pickers, allowing users to set the color for the name of the called student. The set color will be automatically saved.
3. **List Upload**: Supports importing the student list by uploading a file. When uploading, the correct password (current time formatted as HHmm) is required.
4. **Reset Function**: Click the "Reset" button to clear the records of the called students and prepare for the next round of roll call. The correct password is also required.

### Technical Implementation
1. **HTML Part**
    - The page structure is simple and clear, including an area for displaying the called student, a "Roll Call" button, color pickers, a "Reset" button, as well as a button for uploading the list and a hidden file input box.
    - Identify each element through `id` and `class` attributes, which is convenient for operation in CSS and JavaScript.
2. **CSS Part**
    - Use modern Flexbox layout to achieve centered alignment of page elements, making the page responsive on different devices.
    - Add gradient backgrounds and rounded corners to the buttons to enhance the visual effect of the page.
    - Define the style of the color pickers to make them round, which is convenient for users to recognize and operate.
3. **JavaScript Part**
    - **Global Variables**: Define multiple global variables to store and manage roll call status, student lists, the list of called students, the current index, the selected color, and other information.
    - **Time Password Function**: The `getCurrentTimeAsPassword` function is used to obtain the current time and format it into a password format of HHmm, which is used for password verification in list uploading and reset operations.
    - **Roll Call Functions**: The `startRolling` function initiates the roll call scrolling, the `stopRolling` function stops the scrolling and determines the final called student, the `rollNames` function realizes the scrolling display of random student names, and the `callStudent` function determines the final called student and updates the relevant status.
    - **Event Handling**:
        - Add a click event to the "Roll Call" button to check if the list exists and start the roll call process.
        - Add a click event to the color pickers to achieve color selection and saving functions.
        - Add a click event to the "Upload" button to perform password verification and trigger file selection.
        - Add a `change` event to the file input box to read the content of the uploaded file and update the student list.
        - Add a click event to the "Reset" button to perform password verification and reset the roll call status.
    - **Local Storage**: Use `localStorage` to save information such as the list of called students, the current index, the selected color, and the student list, ensuring that data will not be lost after page refresh or closing.

### How to Use
1. Open the web page, and you will see a "Roll Call" button, color pickers, a "Reset" button, and an "Upload List" button.
2. Click the "Upload List" button, enter the password in the current time format (HHmm), and select a text file containing the student list for upload.
3. Click the "Roll Call" button to start the rolling roll call. Finally, the name of an uncalled student will be displayed, and the color of the name can be changed through the color picker.
4. When all students have been called, a prompt "All students have been called. Start a new round." will appear.
5. Click the "Reset" button, enter the password in the current time format, and you can clear the records of the called students and start a new roll call.

### Conclusion
This random roll call web application provides a convenient tool for teachers or other scenarios that require random selection through a simple interface design and rich functionality. At the same time, the code structure is clear, easy to understand and expand, and can be further optimized and customized according to actual needs.  