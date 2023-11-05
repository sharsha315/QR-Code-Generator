'''
QR Code generator using Python
'''

# importing libraries
import qrcode

def generate_qr_code(website_link, output_file="generated_qrcode/your_qrcode.png"):
    """
        This function creates a QR Code image and saves the image in generated_qrcode directory.

        args:
            website-link: The website-link for which the QR code is generated
            output_file: the directory where the QR code is saved, default: 'generated_qrcode/'
    """
    try:
        qr_code = qrcode.QRCode(version = 1, box_size = 5, border = 5)
        qr_code.add_data(website_link)
        qr_code.make()

        qr_image = qr_code.make_image(fill_color = "black", back_color = "white")
        qr_image.save(output_file)
        print(f"QR Code saved as '{output_file}'")
    except Exception as e:
        print(f"An Error occured: {e}")

if __name__ == "__main__":
    website_link = input("Input the website link for the QR Code:\n")
    generate_qr_code(website_link)



