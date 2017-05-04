CREATE OR REPLACE VIEW public.dim_date_cubes AS
 SELECT dim_date.id,
    date_part('year'::text, dim_date."timestamp") AS year,
    date_part('month'::text, dim_date."timestamp") AS month,
    date_part('day'::text, dim_date."timestamp") AS day
   FROM dim_date
  ORDER BY dim_date.id;