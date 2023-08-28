from flask import Flask as F, request as R

A = F(__name__)

@A.route('/')
def f():
    return "Here's the main page. <a href='http://localhost:5000/seeform'>Click here to see the form</a>."

@A.route('/XYZ123', methods=["GET","POST"])
def sF():
    dataStringDATA = """<br><br>
    <form action="" method='POST'>
<input type="text" name="data"> Enter a phrase: <br>
<input type="submit" value="Submit">
"""
    if R.method == "POST":
        pass
    else:
        return dataStringDATA

if __name__ == "__main__":
    A.run(use_reloader=True, debug=True)
