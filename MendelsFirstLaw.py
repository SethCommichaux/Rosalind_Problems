handle = open('Rosalind.txt').read().split()
AA = float(handle[0])
Aa = float(handle[1])
aa = float(handle[2])

total_population = AA + Aa + aa

prob_of_AAxAA = (AA/total_population)*((AA-1.0)/(total_population-1.0))
prob_of_AAxAa = (AA/total_population)*(Aa/(total_population-1.0))
prob_of_AaxAA = (Aa/total_population)*(AA/(total_population-1.0))
prob_of_AAxaa = (AA/total_population)*(aa/(total_population-1.0))
prob_of_aaxAA = (aa/total_population)*(AA/(total_population-1.0))
prob_of_Aaxaa = 0.5*(Aa/total_population)*(aa/(total_population-1.0))
prob_of_aaxAa = 0.5*(aa/total_population)*(Aa/(total_population-1.0))
prob_of_AaxAa = 0.75*(Aa/total_population)*((Aa-1.0)/(total_population-1.0))

prob_of_dom_offspring = prob_of_AAxAA + prob_of_AAxAa + prob_of_AaxAA + prob_of_AAxaa + prob_of_aaxAA + prob_of_Aaxaa + prob_of_aaxAa + prob_of_AaxAa

print prob_of_dom_offspring