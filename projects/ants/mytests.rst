This file holds the tests that you create. Remember to import the python file(s)
you wish to test, along with any other modules you may need.
Run your tests with "python3 ok -t --suite SUITE_NAME --case CASE_NAME -v"
--------------------------------------------------------------------------------

Suite add_insect_multi_bodyguards

	>>> from ants import *
	>>> hive, layout = Hive(AssaultPlan()), dry_layout

	>>> # generates a new colony for each of the cases for manual setup
	>>> default_colony = lambda: AntColony(None, hive, ant_types(), layout, (1, 9))

	>>> # fancy error printing function of the form "{error type}: {error message}"
	>>> print_error = lambda err: print("{0}: {1}".format(type(err).__name__, err))


	Case 1
		>>> colony = default_colony()
		>>> # Testing attempt of adding two bodyguard in the same place, which should fail
		>>> bodyguard_one = BodyguardAnt()
		>>> bodyguard_two = BodyguardAnt()
		>>> colony.places["tunnel_0_0"].add_insect(bodyguard_one)
		>>> try:
		...   colony.places["tunnel_0_0"].add_insect(bodyguard_two)
		... except AssertionError as err:
		...   print_error(err)
		AssertionError: Two ants in tunnel_0_0

	Case 2
		>>> colony = default_colony()
		>>> # Testing attempt of adding a thrower and then two bodyguard in the same place, which should fail
		>>> thrower = ThrowerAnt()
		>>> bodyguard_one = BodyguardAnt()
		>>> bodyguard_two = BodyguardAnt()
		>>> colony.places["tunnel_0_0"].add_insect(thrower)
		>>> colony.places["tunnel_0_0"].add_insect(bodyguard_one)
		>>> try:
		...   colony.places["tunnel_0_0"].add_insect(bodyguard_two)
		... except AssertionError as err:
		...   print_error(err)
		AssertionError: Two ants in tunnel_0_0

	Case 3
		>>> colony = default_colony()
		>>> # Testing attempt of adding a thrower in between the two bodyguard, which should fail
		>>> bodyguard_one = BodyguardAnt()
		>>> thrower = ThrowerAnt()
		>>> bodyguard_two = BodyguardAnt()
		>>> colony.places["tunnel_0_0"].add_insect(bodyguard_one)
		>>> colony.places["tunnel_0_0"].add_insect(thrower)
		>>> try:
		...   colony.places["tunnel_0_0"].add_insect(bodyguard_two)
		... except AssertionError as err:
		...   print_error(err)
		AssertionError: Two ants in tunnel_0_0