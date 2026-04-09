## Jour 1 
### Lundi 30 mars
 - Tutoriel Django (What do you mean :')')
 - Comment facturer gentiment mais correctement en freelance
 - tuples/sets
 - sous quelles conditions push db.sqlite dans un repo
## Jour 2 
### Mardi 31 mars
 - j'ai testé un truc avec git (cf commits), ça a fonctionné mais j'ai du refaire mes venv et les installations en local. Au moins je sais que ça fonctionne maintenant
 - Tutoriel Wagtail Getting Started (What do you mean :')')
 - Tutoriel Wagtail avancé (en cours)
## Jour 3 
### Mercredi 1 avril
 - Suivi des tests et et de correction de bugs sur le project du syndicat du consulat avec Agnès
 - ~~Poursuite~~ Complétion du tutoriel Wagtail avancé.
 - lecture rapide de quelques articles dit "avancés", mais il faudrait les pratiquer sur le terrain
## Jour 4 
### Jeudi 2 avril
 - Première tâche sur un project concret : LeBureau.coop. [Lien GitLab](https://gitlab.com/hashbangfr/lebureau.coop/lebureau) où vous me trouverez sous le pseudo "Den". AAAaaaaaaaa so exited !!!!!!!
 - retirer l'attribut civilités sur site et des formulaires et outils du Bureau
## Jour 5
### Vendredi 3 avril
 - explications sur la gestion des migrations
 - faire en sorte que le prix affiché sur les factures, les mails et le détail sur le site ne se mette pas à jour en fonction des changements (currency) mais reste identique au jour de création de la facture.
 - afin d'être plus friendly avec les nouveaux devs, j'ai ajouté une page d'accueil avec des lien pour la version dev du projet le Bureau. En utilisant Treebeard. cf. Notion : [code that creates content](https://vintage-pot-142.notion.site/Code-that-creates-content-33775e96074380499d77c55f08f14b35?pvs=74).
- corrigé les problèmes avec les merge requests remove civilités (problème de migrations), rendre l'environnement de dev plus sympathique (problème de date réglé par Arthur), et la pipeline de prixcustomerrequest est restée sur un échec ce jour là.
## Jour 6 
### Mardi 7 avril
- régler les problèmes avec la merge request prixcustomerrequest (il faut save() quand tu enregistes manuellement une valeur ma belle)
- commencer à implémenter unfold pour l'admin django sur le bureau.

- ajouter des éléments ForeignKey et ManytoMany en tant qu'autocomplete fields
- découverte des actions unfold (et django au passage). Création du bouton TVA export.

## Jour 7 
### Mercredi 8 avril
- J'ai poursuivi mes aventures avec les actions unfold, en ajoutant le bouton lien_payement, laborieux car il faut comprendre comment fonctionne une permission, en quoi consiste l'action (je n'avais pas compris la veille en fait, j'ai bêtement suivi la documentation, mais c'était déjà un bon début), et les différents fields déclarés dans le ModelAdmin CustomerRequest. Après m'être fait bully par des erreur de type "missing X required positional argument", "KeyError" (je cite Arthur "c'est qu'il y a une erreur de clé :)"), et diverses erreur de reverse et redirection. J'ai passé un super moment. Certaines ont été réglées, d'autres pas encore mais demain sera un nouveau jour.
- J'ai refait les pages de ces deux liens avec unfold, pour qu'elles soient ~~jolies~~ plus user-friendly. Je me suis fait bully par le field datetime, qui apparait comme un champ texte mais requiert une date et une heure dans un format mystère (à toi de le deviner !). J'ai donc expérimenté avec des templates, mais aucun n'a été à la hauteur puisque, naturellement, un calendrier est indispensable. Suite au prochain épisode...

## Jour 8
### Jeudi 9 avril
 - Je repars sur mon lien tva_export qui me répêtait " Reverse for '...' not found. '...' is not a valid view function or pattern name." Je n'ai pas su trouver un moyen de retourner sur la page CustomerRequest autre que simplement lui faire faire un redirect(has_tva_export_permission(request)) aka la fonction associée à cette action qui effectue l'action en question (je me comprends). Bref, ça fonctionne. * danse de la joie *
 - je me souviens ensuite que mon formulaire payment est cassé, en plus de l'absence inacceptable d'un calendrier décent - Arthur m'a aidé à trouver un calendrier mais pour X raison il est vraiment vilain. Affaire à suivre. Revenons au formulaire : ce sont des champs texte qui attendent une date pour d'un, une heure pour l'autre. Si je rentre 12/02/2026 06:22 il me dit 'list' object has no attribute 'stip', et je lui dis oui.
 > ### Leçon du jour
 > Si tu es bloqué
 > Si Internet ne peut te sauver
 > Lis le code source bae.
