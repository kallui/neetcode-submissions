-- Write your query below
-- DISTINCT ON for each unique student_id, keep the first row only (exclusive PSQL feature)
SELECT DISTINCT ON (student_id) student_id, exam_id, score
FROM exam_results
ORDER BY student_id, score DESC, exam_id