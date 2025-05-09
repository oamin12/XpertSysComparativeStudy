from experta import *

class LoanApprovalExpert(KnowledgeEngine):

    @Rule(Fact(cibil_score=P(lambda x: x <= 549.5), 
               loan_term=P(lambda x: x <= 5.0), 
               loan_amount=P(lambda x: x <= 18400000.0), 
               income_annum=P(lambda x: x <= 8050000.0)))
    def rule_0(self):
        print("Loan Status: Rejected")

    @Rule(Fact(cibil_score=P(lambda x: x <= 549.5), 
               loan_term=P(lambda x: x <= 5.0), 
               loan_amount=P(lambda x: x > 18400000.0 and x <= 26250000.0), 
               income_annum=P(lambda x: x <= 8050000.0)))
    def rule_1(self):
        print("Loan Status: Approved")

    @Rule(Fact(cibil_score=P(lambda x: x <= 549.5), 
               loan_term=P(lambda x: x <= 5.0), 
               loan_amount=P(lambda x: x <= 26250000.0),
               income_annum=P(lambda x: x > 8050000.0)))
    def rule_2(self):
        print("Loan Status: Rejected")

    @Rule(Fact(cibil_score=P(lambda x: x <= 549.5), 
               loan_term=P(lambda x: x <= 5.0), 
               loan_amount=P(lambda x: x > 26250000.0), 
               income_annum=P(lambda x: x <= 9650000.0)))
    def rule_3(self):
        print("Loan Status: Approved")

    @Rule(Fact(cibil_score=P(lambda x: x <= 549.5), 
               loan_term=P(lambda x: x <= 5.0), 
               loan_amount=P(lambda x: x > 26250000.0), 
               income_annum=P(lambda x: x > 9650000.0)))
    def rule_4(self):
        print("Loan Status: Approved")

    @Rule(Fact(cibil_score=P(lambda x: x <= 549.5), 
               loan_term=P(lambda x: x > 5.0)))
    def rule_5(self):
        print("Loan Status: Rejected")

    @Rule(Fact(cibil_score=P(lambda x: x > 549.5), 
               residential_assets_value=P(lambda x: x <= 150000.0), 
               commercial_assets_value=P(lambda x: x <= 1850000.0), 
               loan_amount=P(lambda x: x <= 3100000.0)))
    def rule_6(self):
        print("Loan Status: Approved")

    @Rule(Fact(cibil_score=P(lambda x: x > 549.5), 
               residential_assets_value=P(lambda x: 150000.0 < x <= 950000.0), 
               commercial_assets_value=P(lambda x: x <= 1850000.0), 
               loan_amount=P(lambda x: x <= 3100000.0)))
    def rule_7(self):
        print("Loan Status: Approved")

    @Rule(Fact(cibil_score=P(lambda x: x > 549.5), 
               residential_assets_value=P(lambda x: x <= 950000.0), 
               commercial_assets_value=P(lambda x: x <= 1850000.0), 
               loan_amount=P(lambda x: x > 3100000.0), 
               loan_id=P(lambda x: x <= 402.0)))
    def rule_8(self):
        print("Loan Status: Approved")

    @Rule(Fact(cibil_score=P(lambda x: x > 549.5), 
               residential_assets_value=P(lambda x: x <= 950000.0), 
               commercial_assets_value=P(lambda x: x <= 1850000.0), 
               loan_amount=P(lambda x: x > 3100000.0), 
               loan_id=P(lambda x: x > 402.0)))
    def rule_9(self):
        print("Loan Status: Approved")

    @Rule(Fact(cibil_score=P(lambda x: x > 549.5), 
               residential_assets_value=P(lambda x: x <= 950000.0), 
               commercial_assets_value=P(lambda x: x > 1850000.0)))
    def rule_10(self):
        print("Loan Status: Approved")

    @Rule(Fact(cibil_score=P(lambda x: x > 549.5), 
               residential_assets_value=P(lambda x: x > 950000.0)))
    def rule_11(self):
        print("Loan Status: Approved")
