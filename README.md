CI/CD Integrated Cloud Based Income and Expense management System.
Description

The cloud based web application developed using Django Framework and Python 3.9 which provides user to add and manage the income and expense details
Technologies Used

    Python 3
    Django Framework
    SQLite3 Database
    HTML5
    Bootstrap5

Setup Instructions
Clone the repository: git clone https://github.com/PDDeshmukh116/24devopsproject.git
Navigate to the project directory: cd daily_icnome_expense
Install dependencies using pip and the provided requirements.txt file:

pip install -r requirements.txt

Run migrations to set up the database:

python manage.py migrate

Start the development server:

python manage.py runserver

    Access the application at http://localhost:8080 in your web browser.

Project Structure

    /templates: Directory for HTML templates.
    requirements.txt: Lists all Python dependencies for the project.
    buildspec.yml: AWS CodeBuild build specification file.
    sonar-spec.yml: Sonar review configuration file.

Additional Notes

user login creds : username:Pradnyapd1 Password:ppoo1122
