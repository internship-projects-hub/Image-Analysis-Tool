from png_validation import validate_png_file

try:
    validate_png_file("image.png")
    print("PNG validation passed.")
except Exception as e:
    print(f"Validation failed: {e}")
