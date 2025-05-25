Fitness Goal Tracker
How to Use This Repo

Fork this repo:

Go to [your GitHub repo URL] and click the "Fork" button to create a copy in your GitHub account.


Open in Gitpod:

In your forked repo, click the green Code button.
Copy the repo URL (e.g., https://github.com/your-username/fitness-goal-tracker).
Go to gitpod.io/# followed by your repo URL (e.g., gitpod.io/#https://github.com/your-username/fitness-goal-tracker) and press Enter.


Wait for Gitpod to open:

The workspace may take a minute to load. You’ll see a code editor and terminal.


Install dependencies:

In the Gitpod terminal (bottom of the screen), run:pip install flask pandas scikit-learn


Wait for the installation to complete.


Run the app:

In the terminal, run:python app.py


Click the “Open Browser” pop-up or copy the URL (e.g., https://5000-your-workspace-name.gitpod.io) into a browser.


Use the app:

Enter your current weight (kg), target weight (kg), weekly exercise hours, and daily calorie intake.
Click “Predict Time to Goal” to see the estimated weeks to reach your target weight.



Your workspace is ready! Return to it anytime via the Gitpod dashboard. Create only one workspace per project.
Dataset Content
The dataset is synthetic, created for this project to simulate fitness data. Each row represents a user, and each column contains a user attribute. The dataset includes:

Current Weight: The user’s starting weight (kg).
Exercise Hours: Weekly hours spent exercising.
Calorie Intake: Daily calories consumed.
Weeks to Goal: Estimated weeks to reach a target weight (output variable).




Variable
Meaning
Units



current_weight
User’s current weight
70–95 kg


exercise_hours
Weekly hours spent exercising
2–7 hours


calorie_intake
Daily calories consumed
1800–2300 calories


weeks_to_goal
Estimated weeks to reach target weight
8–18 weeks


The dataset is small (10 records) and embedded in app.py for simplicity, suitable for a basic Code Institute project.
Project Terms & Jargon

User: A person using the app to track fitness goals.
Target Weight: The desired weight the user wants to achieve.
Weeks to Goal: The predicted time to reach the target weight.
Churn: Not applicable here, but could refer to users stopping their fitness plan (not modeled in this project).

Business Requirements
As a Data Analyst for Code Institute Consulting, you are tasked by a fitness company to provide a tool for users to predict how long it will take to reach their target weight. The client wants:

A simple app to predict the time (in weeks) to reach a target weight based on current weight, exercise hours, and calorie intake.
Insights into which factors (e.g., exercise hours, calorie intake) most influence the time to reach the goal, to help users adjust their habits.

Hypothesis and How to Validate?

Hypothesis: Users with higher exercise hours reach their target weight faster.
Validation: A correlation study between exercise_hours and weeks_to_goal can confirm this.


Hypothesis: Lower daily calorie intake leads to faster weight loss.
Validation: A correlation study between calorie_intake and weeks_to_goal can confirm this.



Rationale for Mapping Business Requirements to Data Visualizations and ML Tasks

Business Requirement 1: Predict Time to Goal

ML Task: Use a linear regression model to predict weeks_to_goal based on current_weight, exercise_hours, and calorie_intake.
Visualization: (Future enhancement) Plot correlations between input variables and weeks_to_goal to show their impact.
Implementation: The Flask app in app.py uses a trained model to predict weeks based on user inputs via a web form.


Business Requirement 2: Identify Influential Factors

ML Task: Analyze feature importance from the linear regression model to see which inputs (e.g., exercise_hours) most affect predictions.
Visualization: (Future enhancement) Display a bar chart of feature coefficients to highlight key factors.
Implementation: The current app focuses on prediction; feature importance can be added by extracting model coefficients.



ML Business Case
Predict Weeks to Goal
Regression Model

Objective: Predict the number of weeks to reach a target weight based on user inputs (current_weight, exercise_hours, calorie_intake). The target variable (weeks_to_goal) is continuous, so we use a regression model (supervised, uni-dimensional).
Ideal Outcome: Provide users with accurate predictions to plan their fitness goals and help the fitness company offer personalized advice.
Model Success Metrics:
At least 0.7 R² score on train and test sets (not fully evaluated here due to synthetic data).
Failure if predictions are off by more than 50% for 30% of cases after 6 months of real-world use.


Model Output: A number representing weeks to reach the target weight. Users input data via a web form, and predictions are made on the fly.
Heuristics: No prior method exists for predicting time to weight loss goals in this context.
Training Data: A synthetic dataset (10 records) in app.py. Features: current_weight, exercise_hours, calorie_intake. Target: weeks_to_goal.

Dashboard Design (Flask App User Interface)
The app is a single-page Flask application, but the structure aligns with Code Institute’s dashboard expectations.
Page: Fitness Goal Tracker

Purpose: Answer both business requirements.
Features:
Displays a form for users to input current_weight, target_weight, exercise_hours, and calorie_intake.
Shows the predicted weeks to reach the goal or an error if current_weight ≤ target_weight.
(Future enhancement) Add a page to show correlation plots or feature importance.


Implementation: Built with index.html (form and JavaScript), styles.css (styling), and app.py (Flask backend and model).

Notes

This project meets Code Institute’s fifth project requirements for predictive analytics and full-stack development.
The dataset is synthetic for simplicity. For a real project, use a fitness dataset from sources like Kaggle.
Future improvements:
Add data visualizations (e.g., correlation plots using Chart.js).
Deploy to Heroku for Code Institute submission.
Enhance UI with Bootstrap or Tailwind CSS.


To deploy,

