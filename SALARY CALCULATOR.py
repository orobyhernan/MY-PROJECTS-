pe_les : "Personal English lessons"
group_les: "Group Lessons"
hosp_les: "Hospital Lessons"


pe_les = 20
group_les = 20
group_90min_les = 2
hosp_les = 10
remaining_pe_les_from_last_month = 0


hour_rate = 10.08
hosp_hour_rate = 15
tot_pe_les = (((pe_les * 40) / 60) * hour_rate)
tot_group_les = (group_les * hour_rate)
tot_group_90min_les = (((group_90min_les * 90) / 60) * hour_rate)
tot_hosp_les = (hosp_les * hosp_hour_rate)
total_remaining_pe_les_from_last_month = (((remaining_pe_les_from_last_month * 40) / 60) * hour_rate)
total_amount = (tot_pe_les + tot_group_les + tot_group_90min_les + tot_hosp_les + total_remaining_pe_les_from_last_month)
print(total_amount)













