
WITH seasons AS (
	SELECT season_id, season_name
	FROM (VALUES(1,'Winter'),(2,'Winter'),(12,'Winter'),
		 (3,'Spring'),(4,'Spring'),(5,'Spring'),
		 (6,'Summer'),(7,'Summer'),(8,'Summer'),
		 (9,'Fall'),(10,'Fall'),(11,'Fall')
	)AS tbl(season_id, season_name) 
	ORDER BY season_name
),
process_season_matching AS (
	SELECT category, (SELECT season_name FROM seasons WHERE EXTRACT( MONTH FROM sale_date) = season_id) AS season, SUM(quantity) total_quantity, SUM(quantity * price) AS total_revenue 
	FROM sales S
	LEFT JOIN products P ON S.product_id = P.product_id
	GROUP BY category, (SELECT season_name FROM seasons WHERE EXTRACT( MONTH FROM sale_date) = season_id)
),
process_ranking AS (
	SELECT * FROM (
		SELECT category, season, total_quantity, total_revenue, DENSE_RANK() OVER(PARTITION BY season ORDER BY total_quantity DESC, total_revenue DESC) ranking
		FROM process_season_matching
	)sub WHERE ranking = 1
)
SELECT DISTINCT season_name AS season, R.category, R.total_quantity, R.total_revenue
FROM seasons S
LEFT JOIN process_ranking R ON S.season_name = R.season
