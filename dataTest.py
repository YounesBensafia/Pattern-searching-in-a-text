import random
import string
import csv

# Fonction pour générer une chaîne de texte aléatoire d'une longueur donnée
def generate_random_text(length):
    return ''.join(random.choices(string.ascii_uppercase, k=length))

# Fonction pour insérer un motif dans la chaîne de texte
def insert_pattern(text, pattern, num_occurrences):
    positions = random.sample(range(len(text) - len(pattern) + 1), num_occurrences)
    text_list = list(text)
    
    # Insérer le motif aux positions choisies
    for pos in positions:
        for i in range(len(pattern)):
            text_list[pos + i] = pattern[i]
    
    return ''.join(text_list), positions

# Fonction pour générer un jeu de données avec taille de chaîne variable et écrire dans un fichier CSV
def generate_data(num_examples, min_length, max_length, pattern, csv_file):
    data = []
    
    for _ in range(num_examples):
        # Choisir une longueur de chaîne aléatoire dans la plage spécifiée
        text_length = random.randint(min_length, max_length)
        
        # Décider du nombre d'occurrences du motif à insérer (0 à 5)
        num_occurrences = random.randint(0, 5)
        
        # Générer une chaîne de texte aléatoire et y insérer le motif à des positions aléatoires
        random_text = generate_random_text(text_length)
        modified_text, _ = insert_pattern(random_text, pattern, num_occurrences)
        
        # Ajouter les données dans la liste (taille de la chaîne, texte, motif)
        data.append([text_length, modified_text, pattern])
    
    # Trier les données par taille de chaîne en ordre croissant
    data.sort(key=lambda x: x[0])
    
    # Écrire les données générées dans le fichier CSV
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['size_of_string', 'string', 'pattern'])
        writer.writerows(data)

# Exemple : générer 100 exemples, avec une longueur de texte entre 5000 et 10000 caractères, et le motif "XYZ"
generate_data(num_examples=100, min_length=5000, max_length=10000, pattern="XYZ", csv_file="csv/testData.csv")

print("Génération de données terminée. Vérifiez le fichier 'csv/testData.csv'.")
