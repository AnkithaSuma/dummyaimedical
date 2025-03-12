def process(data):
    try:
        patient_name = "Unknown Patient"
        diagnosis = "No diagnosis provided"
        treatment = "No treatment specified"

        if isinstance(data.get("entry"), list):
            for entry in data["entry"]:
                if isinstance(entry, dict):
                    resource = entry.get("resource", {})
                    patient_name = resource.get("patientName", patient_name)
                    diagnosis = resource.get("diagnosis", diagnosis)
                    treatment = resource.get("treatment", treatment)

        result = {
            "case_summary": f"Patient: {patient_name}\nDiagnosis: {diagnosis}\nTreatment: {treatment}"
        }

        print(result)  # ✅ Debugging output
        return result

    except Exception as e:
        print(f"Error: {str(e)}")  # ✅ Debugging error messages
        return {"error": f"Processing error: {str(e)}"}
    
    # Sample JSON data (Replace this with actual data)
data = {
    "entry": [
        {
            "resource": {
                "patientName": "John Doe",
                "diagnosis": "Fractured Arm",
                "treatment": "Cast and rest"
            }
        }
    ]
}

# Call the function and print the output
result = process(data)
print(result)  # This should display the case summary

