import sys
from services.spawn import MobileTemplate
from services.spawn import WeaponTemplate
from resources.datatables import WeaponType
from resources.datatables import Difficulty
from resources.datatables import Options
from java.util import Vector


def addTemplate(core):
	mobileTemplate = MobileTemplate()

	mobileTemplate.setCreatureName('corsec_chief_aggro')
	mobileTemplate.setLevel(83)
	mobileTemplate.setDifficulty(Difficulty.NORMAL)
	mobileTemplate.setMinSpawnDistance(4)
	mobileTemplate.setMaxSpawnDistance(8)
	mobileTemplate.setDeathblow(True)
	mobileTemplate.setScale(1)
	mobileTemplate.setSocialGroup("aggro corsec")
	mobileTemplate.setAssistRange(10)
	mobileTemplate.setStalker(True)
	mobileTemplate.setOptionsBitmask(Options.AGGRESSIVE | Options.ATTACKABLE)

	templates = Vector()
	templates.add('object/mobile/shared_dressed_corsec_captain_human_female_01.iff')
	templates.add('object/mobile/shared_dressed_corsec_captain_human_male_01.iff')
	templates.add('object/mobile/shared_dressed_corsec_captain_human_male_02.iff')
	templates.add('object/mobile/shared_dressed_corsec_captain_human_male_03.iff')
	templates.add('object/mobile/shared_dressed_corsec_officer_human_female_01.iff')
	templates.add('object/mobile/shared_dressed_corsec_officer_human_male_01.iff')
	templates.add('object/mobile/shared_dressed_corsec_detective_human_female_01.iff')
	templates.add('object/mobile/shared_dressed_corsec_detective_human_male_01.iff')
	mobileTemplate.setTemplates(templates)

	weaponTemplates = Vector()
	weapontemplate = WeaponTemplate('object/weapon/ranged/rifle/shared_rifle_e11.iff', WeaponType.RIFLE, 1.0, 20, 'energy')
	weaponTemplates.add(weapontemplate)
	mobileTemplate.setWeaponTemplateVector(weaponTemplates)

	attacks = Vector()
	mobileTemplate.setDefaultAttack('rangedShot')
	mobileTemplate.setAttacks(attacks)
	
	lootPoolNames_1 = ['Junk']
	lootPoolChances_1 = [100]
	lootGroupChance_1 = 100
	mobileTemplate.addToLootGroups(lootPoolNames_1,lootPoolChances_1,lootGroupChance_1)
	
	core.spawnService.addMobileTemplate('corsec_special_ops_chief', mobileTemplate)
	return