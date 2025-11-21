-- estou vendo os clientes com maior frequencia de carregamentos mensais/total e a relaçao com o churn 
SELECT 
customerID, 
MonthlyCharges,
TotalCharges,
CASE
    WHEN Churn = 'No' THEN 0 
    WHEN Churn = 'Yes' THEN 1
END as Churn
from WA_telecom_churn
ORDER by MonthlyCharges DESC