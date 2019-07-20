from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import smtplib, ssl
import time

options = Options()
options.headless = True
browser = webdriver.Chrome(options=options)

#browser = webdriver.Chrome() #replace with .Firefox(), or with the browser of your choice

url_model3 = "https://www.tesla.com/inventory/used/m3?arrangeby=plh&zip=94720&range=0"
url_modelS = "https://www.tesla.com/inventory/used/ms?arrangeby=plh&zip=94720&range=0"
url_new_model3 = "https://www.tesla.com/inventory/new/m3?distance=200&arrangeby=plh&zip=94720&range=0"

url = "http://example.com/login.php"
browser.get(url_new_model3) #navigate to the page

time.sleep(5)

#print dir(browser)

#element = browser.find_element_by_id("<div class='block__elem iso-text--light trimname--label'>Standard Range Plus Rear-Wheel Drive</div>")
#element = browser.find_element_by_css_selector('div.block__elem*')

#element = browser.find_element_by_xpath(//*[@id="iso-container"]/div/div[1]/div[2]/div[2]/span/div/div[1]/div[1]/div[1]/div[1]/div[contains(@class, "block__elem iso-text--light trimname--label"), text()='Standard Range Plus Rear-Wheel Drive'])
elements = browser.find_elements_by_xpath("//div[contains(@class, 'block__elem')]")
#	"block__elem iso-text--light trimname--label")

#print type('element.text: {0}'.format(element.text))

for i in elements:
	print i.text
#print "Long Range Plus Rear-Wheel Drive" in element.text

if len(elements) > 0:
	# Replace sender@example.com with your "From" address.
	# This address must be verified with Amazon SES.
	SENDER = "Sender Name <blah@gmail.com>"

	# Replace recipient@example.com with a "To" address. If your account 
	# is still in the sandbox, this address must be verified.
	RECIPIENT = "blah@gmail.com"

	# Specify a configuration set. If you do not want to use a configuration
	# set, comment the following variable, and the 
	# ConfigurationSetName=CONFIGURATION_SET argument below.
	#CONFIGURATION_SET = "ConfigSet"

	# If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
	AWS_REGION = "us-west-2"

	# The subject line for the email.
	SUBJECT = "Amazon SES Test (SDK for Python)"

	# The email body for recipients with non-HTML email clients.
	BODY_TEXT = ("Amazon SES Test (Python)\r\n"
	             "This email was sent with Amazon SES using the "
	             "AWS SDK for Python (Boto)."
	            )
	            
	# The HTML body of the email.
	BODY_HTML = """<html>
	<head></head>
	<body>
	  <h1>Amazon SES Test (SDK for Python)</h1>
	  <p>This email was sent with
	    <a href='https://aws.amazon.com/ses/'>Amazon SES</a> using the
	    <a href='https://aws.amazon.com/sdk-for-python/'>
	      AWS SDK for Python (Boto)</a>.</p>
	</body>
	</html>
	            """ 	

	# The character encoding for the email.
	CHARSET = "UTF-8"

	# Create a new SES resource and specify a region.
	client = boto3.client('ses',region_name=AWS_REGION)

	# Try to send the email.
	try:
		#Provide the contents of the email.
		response = client.send_email(
			Destination={
				'ToAddresses': [
					RECIPIENT,
				],
			},
			Message={
				'Body': {
					'Html': {
						'Charset': CHARSET,
						'Data': BODY_HTML,
					},
					'Text': {
						'Charset': CHARSET,
						'Data': BODY_TEXT,
					},
				},
				'Subject': {
					'Charset': CHARSET,
					'Data': SUBJECT,
				},
			},
			Source=SENDER,
			# If you are not using a configuration set, comment or delete the
			# following line
			ConfigurationSetName=CONFIGURATION_SET,
		)

	# Display an error if something goes wrong.	
	except ClientError as e:
	    print(e.response['Error']['Message'])
	else:
	    print("Email sent! Message ID:"),
	    print(response['MessageId'])


browser.quit()
