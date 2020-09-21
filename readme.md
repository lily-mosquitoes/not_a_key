# Not a Key

Not a Key is a taxonomic identification tool, similar to a paper-based dichotomous key, but *dynamic*.

The need for something like this arose from mosquito (Diptera: Culicidae) identification. Many different professionals (non-taxonomists) have a need to identify mosquitoes rapidly and accurately, but often lack the training in mosquito taxonomy to do so using primary resources, and resort to usage of 'lab keys', often massively reduced in scope and lacking updates in recent taxonomic developments.

The issues with usage of 'lab keys' further compound with all the issues related to *paper-based keys* in general: they are one-dimensional, carry character choice bias from authors, and are frozen snapshots of the local richness of species at the time of publication.

This project is an effort to fix or mitigate some of these issues:
* The identification tool relies on a database of character states to construct paths (trees) on the fly; each character choice you make affects which couplet you may be shown next.
* The tool also relies on a database of species occurrences, and as such allow the user to reduce the scope of their search without losing information.
* Both databases can be synchronized with online databases, and thus the information is ever changing and if well maintained and supported, it can always be up to date with developments in taxonomy and known species distributions.

Although this tool was conceptualized to aid with mosquito identification by non-taxonomists, it is being developed as a general identification tool, that implements the basic *look and feel* of a paper-based dichotomous key, with the advantages of a non-linear, dynamically generated "key-out" path, and easily updatable information.

This aims to be a robust tool to provide accurate identification to users with minimal training in taxonomy in a given group.

## The Project

The project currently consists of four main parts:

1. The Not a Key identification tool
   * this tool queries a database of character states, dubbed the *key database*
   * and it queries a database of species occurrences, dubbed the *reference database*
   * it is a general tool which will be able accept well defined *resources* for identification of any organisms that can be identified with a paper-based key

2. The Key Database
   * the structure of the database of character states is simple and concise, it's job is to allow us to describe any species with a series of defined states for character couplets.
   * the database of character states is undoubtedly they linchpin of this project, however, such data sets don't usually exist for identification-value characters, this was the case for mosquitoes.
   * building and maintenance of a *key database* for mosquitoes is being facilitated through the Key Database Manager tool, developed to make updating the *key database* accessible.
   * building a *key database* with a high number of couplets that are easy to understand and overlapping in species coverage is essential for achieving the desired goals of the project.

3. [The Key Database Manager tool](https://github.com/lily-mosquitoes/key_database_manager#key-database-manager)
   * this tool was developed to help people involved with the project easily help to build and maintain the *key database* for mosquito identification.

4. The Reference Database
   * the structure of the database of species occurrences is designed to be small, and contain the least amount of data necessary to allow the features envisioned for the Not a Key to work.
   * sourcing this data for any group is a challenge, and mosquitoes are not the exception; fortunately, through a conjoined effort of all entities within the [Midwest Center of Excellence for Vector-Borne Disease](http://mcevbd.wisc.edu/about), the hope is that the Not a Key will be released with a *mosquito identification resource* containing a *reference database* that will provide accurate data for mosquito species distribution for the Upper Midwest of the US.

## Features

**Skip button:** for when you don't feel comfortable making a call in a couplet, or the structure was simply lost.
* *It is important to note that skipping can be only allowed when more than one couplet is able to distinguish a given set of possible species; in other words, the more couplets a key database has and the more overlap they have in identifying species, the instances where a user is allowed to skip a couplet are likely to increase*

**Back button:** for when you made a mistake, or just want to check another path.

**Couplet weighing:** couplets in the *key database* have weights which translate to how trusted they are; making a choice at a couplet which is considered difficult to accurately interpret result in the species for which the not chosen state is present being put in a separate list, "possible, if mistaken". This list is considered by the algorithm choosing the next couplets and species in it may consistently get removed by the next choices, confirming your choice was correct, or not, which *can* be *an indicative* of mistakenly identified character states.

**Abundance data:** lists of possible species are displayed with abundance data attached. This information is gathered from the *reference database* applying the chosen filters for location and time frame; and it will be only as accurate as the data itself. Take note that species with abundance of zero will show up, this is by design. The location filtering cuts off species shown, but the time frame filtering only prevents species from being counted towards abundance information given, but they are still considered, as to avoid missing identification of species that may occur at a month or season not yet recorded.

**Location selection:** for the *mosquito identification resource* locations are divided into US states, this seems like the lowest resolution reasonable for the goal of this project, that is, to provide a reliable identification resource for the user and allow maintainers to easily keep the databases up to date.

**Time frame selection:** users can choose to show abundance information, which may be taken into account by the key when choosing the next couplet, and/or by the user when deciding to stop at an earlier point than the end of the key-out. The selection options are to filter species by month or by season.

**Multiple couplet choosing algorithms:** users can choose between different available algorithms that perform the task of choosing the next "best" couplet based on the given species list to be tackled at any given point. This may be useful to distinguish between different use cases for the tool, for example, when one wants to reach any species as fast as possible versus when one wants to prioritize identifying the most abundant species. It is easy to integrate new algorithms to this software, and the selection may grow as time passes; however, at this time they are intrinsic to the software and introduction of new algorithms to users will need to come in new releases.

**Multiple resources:** users will be able to install multiple *identification resources*; in accordance with the starting goal of this project, the tool will be released with a *mosquito identification resource*. The hope is that more people will build and maintain resources for this tool.

## Acknowledgments

Special thanks to Lyric Bartholomay, Chris Stone, Andrew Mackay and Corrado Cara for supporting the project and providing feedback.

Thanks to the [Midwest Center of Excellence for Vector-Borne Disease](http://mcevbd.wisc.edu/about) for providing financial support for the Not a Key Project.
