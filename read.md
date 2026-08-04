# HTML-Project
## A simple Flask web application demonstrating how to trigger a backend Python function using an HTML form submit button.

## 📁 Project Structure
For Flask to locate and render your HTML files correctly, you **must create a folder named `templates`** in your project root and place `index.html` inside it[cite: 1, 2].

```text
flask-submit-demo/
│
├── app.py              # Main Flask application logic
└── templates/          # Folder required by Flask for HTML files
    └── index.html      # Frontend HTML template
```
🛠️ How It Works
1. HTML Form (templates/index.html)The frontend contains a simple <form> element. Setting method="POST" and pointing the action attribute to /run-script ensures that clicking the submit button sends a request to the backend route:
   ```
   HTML
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <title>Run Python Script</title>
   </head>
   <body>
        <h1>Trigger Python Code</h1>

   <!-- The form sends a POST request to /run-script when clicked-->
   <from action="/run-script" method="POST">
        <button type="submit">Submit and Run Python</button>
     </form>
   </body>
   </html>
   ```
  ## Flask Backend (app.py)
The Flask application defines two routes:  
1. ``GET /``: Renders the index.html file from the templates/ directory.
2. ``POST /run-script``: Listens for the form submission, executes custom Python code, and returns the result to the user.
3. You can view the main application logic in [`app.py`](app.py).
  
