from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Define colors dynamically
    header_background_color = "#333"
    header_text_color = "#fff"
    nav_link_color = "#333"
    section_heading_color = "#333"
    footer_background_color = "#fff"
    footer_text_color = "black"

    # Pass colors to the template
    return render_template('index.html',
                           header_background_color=header_background_color,
                           header_text_color=header_text_color,
                           nav_link_color=nav_link_color,
                           section_heading_color=section_heading_color,
                           footer_background_color=footer_background_color,
                           footer_text_color=footer_text_color)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
