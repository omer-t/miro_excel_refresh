select
    reported_at_date,
    account_id,
    account_name,
    campaign_id,
    campaign_name,
    campaign_status,
    adgroup_id,
    adgroup_name,
    adgroup_type,
    adgroup_status,
    sum(spend)              as spend,
    sum(impressions)        as impressions,
    sum(link_clicks)        as link_clicks,
    sum(users)              as users,
    sum(corporate_users)    as corporate_users,
    sum(work_users)         as work_users,
    sum(team_leader_users)  as team_leader_users
from
    production.marketing.paid_search
where 1=1
    and reported_at_date
        between '2021-06-01'
        and     '2022-08-01'
group by
    1,2,3,4,5,6,7,8,9,10