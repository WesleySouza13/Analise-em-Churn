--selecionando informa~coes sobre serviços contratados por cliente
SELECT 
customerID,
PhoneService, 
MultipleLines,
InternetService,
OnlineSecurity, 
OnlineBackup,
DeviceProtection, 
TechSupport,
StreamingTV,
StreamingMovies,
CASE
    WHEN Churn = 'No' THEN 0
    WHEN Churn = 'Yes' THEN 1
end as Churn
from WA_telecom_churn
