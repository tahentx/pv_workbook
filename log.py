import logging
logging.basicConfig(level=logging.INFO)
# Create function that converts dollars to cents
def convert_dollars_to_cents(dollars):

    # Try...
    try:
        # Multiply dollars by 100
        cents = dollars * 100

        # Convert to integer
        cents = int(cents)

        # Send info message that function was run successful
        logging.info("convert_dollars_to_cents run successfully")

        # Return cents
        return cents

    # If a ValueError is raised
    except ValueError:

        # Create data type of input
        dollars_type = type(dollars)

        # Create error message detailing the error
        error_message = f"Function input is {dollars_type}, should be <class \'int\'>"

        # Send error message
        logging.error(error_message)

convert_dollars_to_cents(12.45)
