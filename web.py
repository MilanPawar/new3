import cv2
import mysql.connector 
from selenium import webdriver

# # Connect to the database
# connection = mysql.connector.connect(
#     host="your_host",
#     user="your_username",
#     password="your_password",
#     database="your_database"
# )

# # Create a cursor object
# cursor = connection.cursor()

# # Define the SQL query
# query = "SELECT username, password FROM users WHERE id = %s"

# # Execute the query
# cursor.execute(query, (user_id,))

# # Fetch the result
# result = cursor.fetchone()

# # Close cursor and connection
# cursor.close()
# connection.close()

# # Process the result
# if result:
#     username, password = result
#     print("Username:", username)
#     print("Password:", password)
# else:
#     print("User not found")
# # from selenium import webdriver
# # from webdriver_manager.chrome import ChromeDriverManager

# # options = webdriver.ChromeOptions()
# # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

# print(cv2.__version__)


# Initialize Chrome WebDriver
driver = webdriver.Chrome()
driver.get("https://www.ebay.com")
driver.save_screenshot("screenshot.png")
driver.quit()


