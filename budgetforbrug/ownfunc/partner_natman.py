from os.path import join
from dataclasses import dataclass, field


@dataclass
class BasisOpl:
    pathroot: str = r"C:\Filkassen"
    dirname_fr: str = "1. Financial Report"
    dirname_inv: str = "2. Invoices and support Doc"
    dirname_tim: str = "3. Timesheets"


@dataclass
class Natureman(BasisOpl):
    pathbase: str = r"LIFE-NatureMan Financial Reporting"
    dirname_fr: str = join("Fase 3 2022og2023", BasisOpl.dirname_fr)
    distspec: dict = field(
        default_factory=lambda: {
            "Jam": "1. Jammerbugt Kommune",
            "Mar": "2. Mariagerfjord Kommune",
            "Ran": "3. Randers Kommune",
            "Reb": "4. Rebild Kommune",
            "Ski": "5. Skive Kommune",
            "Vhi": "6. VestHimmerland Kommune",
            "Vib": "7. Viborg Kommune",
            "Aal": "8. Aalborg Kommune",
            "NST": "91. Naturstyrelsen",
            "LBST": "92. Landbrugsstyrelsen",
            "MST": "93. Miljostyrelsen",
        }
    )

    def get_file_path(self, partner):
        file_name = join(
            BasisOpl.pathroot, self.pathbase, self.distspec[partner], self.dirname_fr
        )
        return file_name
