# Binder example for calculating molarity

def calculate_molarity(moles, volume):
    return moles / volume

# Example usage
moles = float(input("Enter moles of solute (mol): "))
volume = float(input("Enter volume of solution (L): "))
molarity = calculate_molarity(moles, volume)
print(f'Molarity: {molarity} M')
