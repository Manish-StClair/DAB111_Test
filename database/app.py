{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Week 12a: GitHub overview and setup\n",
    "\n",
    "### Practice repo\n",
    " - create new virtual environment for project\n",
    " - download and install Git \n",
    " - basics of Git and GitHub\n",
    " - sign in to GitHub\n",
    " - create a **PRACTICE** repo(sitory)\n",
    "    - with `gitignore`\n",
    "    - with `readme.md`\n",
    " - open *GitHub for Desktop*\n",
    " - clone the repository just created\n",
    "    - use `.\\Documents\\GitHub` as the file location\n",
    "    - may need to sign in again\n",
    " - modify `readme.md`\n",
    " - commit and push changes to GitHub\n",
    " - view changes on GitHub\n",
    " - create project folders\n",
    " - commit and push changes to GitHub\n",
    " - view changes on GitHub\n",
    " - email link and view\n",
    " - add a collaborator\n",
    "    - settings\n",
    "    - Collaborators\n",
    " - collaborator\n",
    "   - clone the other repository\n",
    "   - make a change\n",
    "   - commit and push change to GitHub\n",
    "   - view change on GitHub\n",
    "\n",
    " ### Project repo\n",
    "\n",
    "  - only **ONE** per group\n",
    "    - one person creates\n",
    "    - then add other group members as Collaborators\n",
    "  - project submission \n",
    "     - submit link to project repo\n",
    "\n",
    "### Tips\n",
    " - commit (error-free) changes often so GitHub master repo is never too out of dat\n",
    " - don't have people work on the same code at the same time\n",
    " - speak to each other frequently about what each of you are working on "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: flask in e:\\anaconda\\envs\\dab111\\lib\\site-packages (3.0.0)\n",
      "Requirement already satisfied: Werkzeug>=3.0.0 in e:\\anaconda\\envs\\dab111\\lib\\site-packages (from flask) (3.0.1)\n",
      "Requirement already satisfied: Jinja2>=3.1.2 in e:\\anaconda\\envs\\dab111\\lib\\site-packages (from flask) (3.1.2)\n",
      "Requirement already satisfied: itsdangerous>=2.1.2 in e:\\anaconda\\envs\\dab111\\lib\\site-packages (from flask) (2.1.2)\n",
      "Requirement already satisfied: click>=8.1.3 in e:\\anaconda\\envs\\dab111\\lib\\site-packages (from flask) (8.1.7)\n",
      "Requirement already satisfied: blinker>=1.6.2 in e:\\anaconda\\envs\\dab111\\lib\\site-packages (from flask) (1.7.0)\n",
      "Requirement already satisfied: colorama in e:\\anaconda\\envs\\dab111\\lib\\site-packages (from click>=8.1.3->flask) (0.4.6)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in e:\\anaconda\\envs\\dab111\\lib\\site-packages (from Jinja2>=3.1.2->flask) (2.1.1)\n"
     ]
    }
   ],
   "source": [
    "!pip install flask"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "from flask import Flask"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "app = Flask(__name__)\n",
    "\n",
    "@app.route('/')\n",
    "def index():\n",
    "    return \"Hello, World\"\n",
    "\n",
    "if __name__==\"__main__\":\n",
    "    app.run(debug=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
