# mtg-self-play
self play simulation and bot training environment for mtg


This has several parts:
   1. Roger, a platform for creating, training and managing bots
   2. M-Sim, a self-contained simulation environment
   3. Uras, a fast database of cards.

Uras:
   Crawlers:
      A set of crawlers update card data, formats and metadata and marketplace links.

   Query API:
      A canonical M-sim card_id is used to query Uras
   
M-sim:
  Provides an API into simulations, including full control for up to 4 players, and on-going self-play training

Roger:
  Provides an API for creating, training and managing a population of mtg bots.

  Bot interface includes self-play controls as well as real-time decision support (companion app) functionality.
   
