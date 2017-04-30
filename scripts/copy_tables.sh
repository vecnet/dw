#!/usr/bin/env bash

SOURCE=dw1
TARGET=dw2
# Run as postgres user
# sudo -u postgres bash copy_tables.sh
/usr/pgsql-9.3/bin/pg_dump -t dim_date $SOURCE | /usr/pgsql-9.3/bin/psql -d $TARGET
/usr/pgsql-9.3/bin/pg_dump -t dim_location $SOURCE | /usr/pgsql-9.3/bin/psql -d $TARGET
/usr/pgsql-9.3/bin/pg_dump -t dim_source $SOURCE | /usr/pgsql-9.3/bin/psql -d $TARGET
/usr/pgsql-9.3/bin/pg_dump -t dim_subgroup $SOURCE | /usr/pgsql-9.3/bin/psql -d $TARGET
/usr/pgsql-9.3/bin/pg_dump -t dim_type $SOURCE | /usr/pgsql-9.3/bin/psql -d $TARGET
/usr/pgsql-9.3/bin/pg_dump -t dim_user $SOURCE | /usr/pgsql-9.3/bin/psql -d $TARGET
/usr/pgsql-9.3/bin/pg_dump -t dim_weather_station $SOURCE | /usr/pgsql-9.3/bin/psql -d $TARGET
/usr/pgsql-9.3/bin/pg_dump -t fact_demographics $SOURCE | /usr/pgsql-9.3/bin/psql -d $TARGET
/usr/pgsql-9.3/bin/pg_dump -t fact_gross_national_income $SOURCE | /usr/pgsql-9.3/bin/psql -d $TARGET
/usr/pgsql-9.3/bin/pg_dump -t fact_households $SOURCE | /usr/pgsql-9.3/bin/psql -d $TARGET
/usr/pgsql-9.3/bin/pg_dump -t fact_pacrain_rainfall $SOURCE | /usr/pgsql-9.3/bin/psql -d $TARGET
/usr/pgsql-9.3/bin/pg_dump -t fact_weather $SOURCE | /usr/pgsql-9.3/bin/psql -d $TARGET
/usr/pgsql-9.3/bin/pg_dump -t fact_wmr_act_oprtnl_cvrg $SOURCE | /usr/pgsql-9.3/bin/psql -d $TARGET
/usr/pgsql-9.3/bin/pg_dump -t fact_wmr_hh_surveys $SOURCE | /usr/pgsql-9.3/bin/psql -d $TARGET
/usr/pgsql-9.3/bin/pg_dump -t fact_wmr_irs_oprtnl_cvrg $SOURCE | /usr/pgsql-9.3/bin/psql -d $TARGET
/usr/pgsql-9.3/bin/pg_dump -t fact_wmr_itn_oprtnl_cvrg $SOURCE | /usr/pgsql-9.3/bin/psql -d $TARGET
/usr/pgsql-9.3/bin/pg_dump -t gis_base_table $SOURCE | /usr/pgsql-9.3/bin/psql -d $TARGET
/usr/pgsql-9.3/bin/pg_dump -t lut_entomological_endpoint $SOURCE | /usr/pgsql-9.3/bin/psql -d $TARGET
/usr/pgsql-9.3/bin/pg_dump -t lut_intervention_irs_coverage_admin1 $SOURCE | /usr/pgsql-9.3/bin/psql -d $TARGET
/usr/pgsql-9.3/bin/pg_dump -t lut_intervention_itn_coverage_admin1 $SOURCE | /usr/pgsql-9.3/bin/psql -d $TARGET
/usr/pgsql-9.3/bin/pg_dump -t lut_repr_workflow_parameters $SOURCE | /usr/pgsql-9.3/bin/psql -d $TARGET
/usr/pgsql-9.3/bin/pg_dump -t lut_map_siteid $SOURCE | /usr/pgsql-9.3/bin/psql -d $TARGET
/usr/pgsql-9.3/bin/pg_dump -t lut_species $SOURCE | /usr/pgsql-9.3/bin/psql -d $TARGET
/usr/pgsql-9.3/bin/pg_dump -t lut_vector_sensitivity_parameters $SOURCE | /usr/pgsql-9.3/bin/psql -d $TARGET
/usr/pgsql-9.3/bin/pg_dump -t lut_vector_species_parameter $SOURCE | /usr/pgsql-9.3/bin/psql -d $TARGET
