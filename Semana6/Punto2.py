salary1 = int(input("¿Cuántos salarios de tipo 1 debe pagar? "))
salary2 = int(input("¿Cuántos salarios de tipo 2 debe pagar? ")) 
salary3 = int(input("¿Cuántos salarios de tipo 3 debe pagar? "))

p_salary1 = 100000
p_salary2 = 50000
p_salary3 = 200000
comision = 20000
n_comisiones = int(input("¿Cuántos comisionan? "))
social_s = 0.12

t_salary1 = salary1 * p_salary1
t_salary2 = salary2 * p_salary2
t_salary3 = salary3 * p_salary3

trabajadores = salary1 + salary2 + salary3
g_salary = t_salary1 + t_salary2 + t_salary3
t_social_s = g_salary * social_s                                                                                                                        

t_comision = n_comisiones * comision                

total = g_salary + t_comision + t_social_s

print(f"Debe pagar {trabajadores} salarios.")
print(f"{salary1} de tipo 1, {salary2} de tipo 2, y {salary3} de tipo 3.")
print(f"Esto equivale a un total de: {g_salary:,.2f}")
print(f"A esto se debe sumar {t_comision:,.2f} de comisiones.") 
print(f"{t_social_s:,.1f} de seguridad social.")  
print(f"Total: {total:,.2f}")  

