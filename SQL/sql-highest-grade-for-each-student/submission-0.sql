-- Write your query below
-- NON PSQL solution, use ROW_NUMBER() OVER ...

SELECT student_id, exam_id, score
FROM (SELECT 
        student_id, exam_id, score,
        ROW_NUMBER() OVER (
            PARTITION BY student_id
            ORDER BY score DESC, exam_id ASC
        ) AS ranked
    FROM exam_results
    ) AS ranked_table
WHERE ranked = 1
ORDER BY student_id ASC