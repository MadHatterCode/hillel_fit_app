def registration_form():
    return f"""<form action="/register" method="post"">
                  <label for="login">Login:</label><br>
                  <input type="text" id="login" name="login"><br>
                  <label for="password">Password:</label><br>
                  <input type="password" id="password" name="password"><br>
                  <label for="birth_date">Birth date:</label><br>
                  <input type="date" id="birth_date" name="birth_date"><br>
                  <label for="phone">Phone:</label><br>
                  <input type="text" id="phone" name="phone"><br>
                  <input type="submit">
                </form>"""
