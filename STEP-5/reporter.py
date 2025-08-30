# src/reporter.py

import json
import os
from datetime import datetime

class ReportGenerator:
    """
    Generates a comprehensive JSON report from the analysis and simulation data.
    """
    def __init__(self, parsed_data, validation_results, output_dir='reports'):
        self.parsed_data = parsed_data
        self.validation_results = validation_results
        self.output_dir = output_dir

    def generate_json_report(self):
        """
        Compiles all data into a single dictionary and saves it as a timestamped JSON file.
        """
        print("\nStep 5: Generating comprehensive analysis report...")
        
        # Ensure the output directory exists
        os.makedirs(self.output_dir, exist_ok=True)

        # Structure the final report
        report = {
            "report_metadata": {
                "timestamp": datetime.now().isoformat(),
                "title": "Comprehensive Network Analysis Report"
            },
            "parsed_configurations": self.parsed_data,
            "validation_summary": self._format_validation_summary()
        }
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(self.output_dir, f'comprehensive_analysis_{timestamp}.json')

        try:
            with open(filename, 'w') as f:
                json.dump(report, f, indent=4)
            print(f"✅ Comprehensive JSON report saved to '{filename}'")
        except TypeError as e:
            print(f"❌ Error generating JSON report: {e}. Check data for non-serializable types.")
        except Exception as e:
            print(f"❌ An unexpected error occurred while writing the JSON report: {e}")

    def _format_validation_summary(self):
        """Creates a clean summary of validation results for the report."""
        summary = {}
        for check, issues in self.validation_results.items():
            summary[check] = {
                "status": "issues_found" if issues else "no_issues",
                "count": len(issues),
                "details": issues
            }
        return summary
