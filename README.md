# Flask Name and Number Input App

A simple Flask web application that accepts a user's name and number via an HTML form, processes the submission on the backend, and displays the submitted data in an output box on the same page.

---

## 📁 Project Structure

For Flask to locate and render your HTML files properly, make sure to **create a folder named `templates`** in your project root and place `index.html` inside it[cite: 3, 4].

```text
flask-name-number-app/
│
├── app.py              # Flask server and route logic
└── templates/          # Directory required by Flask for HTML files
    └── index.html      # Frontend template with form and output display
```
## 🛠️ How It Works
### 1. HTML form & Templates (templates/index.html)

The HTML page contains two main sections styled as side-by-side boxes:
* Input Box: Contains an HTML ` <form>` using ` method="POST" ` with inputs for ` name_input ` and ` number_input `.
* Output Box : Uses Jinja2 conditional rendering `({% if name and number is not none %} ) ` to display the submitted values, or a fallback message if no data has been submitted yet.
* You can View the generated HTML at .[`HTMLCode)`](HTMLCode). 

## 2. Flask Backend
The single Flask route (/) handles both GET and POST requests:
1.GET Request: Renders the empty template when first visiting the page.
2.POST Request: Extracted inputs from ` request.form.get()` (`name_input and number_input`) are stored and passed back into `render_template()` as the `name` and `number` variables to be rendered on screen.

## 3. Run a python code with a generated code from Chatgpt or such AI engines but for reference I will list one below
 * You can view the python code at [`app.py2)`](app.py2).
## 4. 🚀 How to Run Locally
1. Install flask:
   `` pip install flask ``
2. Run the application:
   `` python app.py``
3. Open the browser on the provided URL , enter your name and a number, and click Submit to view the result rendered in the output box.
