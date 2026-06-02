SELECT
    categorie,
    SUM(quantite) AS total_quantite,
    SUM(chiffre_affaires) AS total_ca
FROM {{ ref('ventes_clean') }}
GROUP BY categorie