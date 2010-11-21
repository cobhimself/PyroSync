#PyroSync

PyroSync is a wrapper for the rsync command line utility that allows you to save
preset rsync commands to be run again in the future. It is currently under
development.

##SYNOPSIS `pyrosync.py [OPTIONS] [VERB] presetName(s)`


##OPTIONS:

`-h`, `--help` Displays the PyroSync help information

`-Y`, `--assume-yes` Automatically assume 'Yes' at any prompt for verification.
This is helpful for batch scripts.

`-n`, `--dry-run` Tells PyroSync to pass on the `dry-run` option to rsync. This
causes a preset to only show what would have been synchronized.

`-p`, `--preview` PyroSync will only echo the rsync commands that are generated
from the given preset names.

NOTE: This only applies to the PyroSync script.  It does not run the rsync
command represented by this preset and automatically add the --dry-run argument
to each preset's rsync options list.

##VERBS

PyroSync contains four different verbs (or functions) that allow you to interact
with the presets you've created or want to create. The verbs that currently
exist are listed below:

* run (default verb. No need to specify)
* add
* delete
* edit
* list

###run

To run a preset, pass PyroSync one or more preset names:

    pyrosync presetName1 "Preset Name2" presetName3 ...

The presets will be executed in the order they were given.

NOTE: You do not pass the `run` verb. When PyroSync sees that no other verb has
been sent, it autmatically assumes you mean to run the given preset(s). Also,
any presets that contain spaces in their name will need to be given within
quotes.

###add

The `add` verb of PyroSync takes arguments in two different formats. When only
the preset name is provided, PyroSync launches an interactive prompt that allows
you to enter in the information about the preset.

    pyrosync add "presetName"

You can also specify all the details about a preset in one `add` command:

    pyrosync add "My Preset" /Source/Folder/ /Destination/Folder/ "This is the
    description for My Preset" -auhvPE --exclude=.* --other --rsync --options
    --as --needed

###delete

To delete a preset, send one or more preset names:

    pyrosync delete presetName1 "Preset Name2" presetName3 ...

NOTE: Any presets that contain spaces in their name will need to be given within
quotes.

###edit

To edit a preset, use the `edit` verb and send a preset name:

    pyrosync edit presetName
    
###list

To see a list of the available presets, use the `list` verb:

    pyrosync list

When the list verb is used, a concise listing of the preset names are output to
the user. To see a more detailed listing, send the `list` verb one of the
following values:

* `more` - list more information about the presets. This includes the individual
  properties of each of the presets
* `all` - list all of the information about the presets. This includes the
  individual properties of each of the presets as well as the final rsync
  command that will be used.

##EXAMPLES:

###ADDING PRESETS:

Add a preset by name and then fill in the properties through prompts:

    pyrosync.py -n "My Preset"

    pyrosync.py -n MyPresetName

Add a preset and its properties in one go:

    pyrosync.py -n "My Preset" /Source/Folder/ /Destination/Folder "This is the
    description for My Preset" -auhvPE --exclude=.* --other --rsync --options
    --as --needed

The options to be used with the defined rsync command are to be declared after
the description of the current preset. PyroSync then takes these arguments and
consolidates them and adds them as the options for the rsync preset.

###VIEWING PRESETS:

List all preset names:

    pyrosync list

List all preset names and the preset's properties:

    pyrosync list more

List all preset names, the presets's properties and the generated rsync command:

    pyrosync list all

###PREVIEWING PRESETS

To preview a preset:

    pyrosync -p "My Preset"

To preview multiple presets

    pyrosync -p "My Preset" "My Second Preset" Preset1 Preset2 [...]

###RUNNING PRESETS

To run a preset:

    pyrosync "My Preset"

To run multiple presets

    pyrosync "My Preset" "My Second Preset" Preset1 Preset2 [...]

###DELETING PRESETS

Unless the `-Y` or `--assume-yes` arguments are assigned, you will be prompted
to confirm that you would like to carry out the deletion function.

To delete a preset:

    pyrosync delete "My Preset"

To delete multiple presets:

    pyrosync delete "My Preset" "My Second Preset" Preset1 Preset2 [...]

NOTE: A list of successfully deleted presets as well as any unknown presets will
be printed to the screen.

###EDITING PRESETS

To edit a preset:

    pyrosync edit presetName

When editing a preset, you will be given the opportunity to edit the preset's
name, description, rsync options and the source and destination locations for
rsync to use.

#BUGS

You can submit any bugs you find to
https://github.com/cobhimself/PyroSync/issues

#ROAD MAP

PyroSync is currently in development. The following are hopefully what is in
store:

##Version 1.0

* All verbs will be bug-free and will operate as you'd expect.

##Version 1.1

* Export presets. The user will have the ability to export any PyroSync presets
  that they have created.
* Import presets. The user will have the ability to import any PyroSync presets
  that they have created.
* Dynamic data. The user will be able to add dynamic information to the saved
  rsync commands. Things like date, and directory information.

#AUTHOR

PyroSync was written by Collin D. Brooks <collin.brooks@gmail.com>.

#SEE ALSO rsync(1)
