RadioButton
===========
RadioButton widgets are similar to CheckButton's, however they allow only one of a group of RadioButton's to be selected at any one time. When another RadioButton in the group is selected, the active state of the button is switched to that and removed from the previous one which was chosen.

===========
Constructor
===========
The RadioButton can be constructed using the following::

  radiobutton = Gtk.RadioButton(label, group, use_underline)

The *label* value should be set to describe the function of the RadioButton. The *group* parameter is set to the name of the first RadioButton to be included in the group. For the first RadioButton, this should be set to ``None``. Subsequent RadioButton widgets should then have their group parameter set to the name of the first RadioButton. When *use_underline* is set to ``True``, the character preceded by an underscore will be marked as the accelerator character.

=======
Methods
=======
To join a RadioButton to a group after construction use::

  radiobutton.join_group(group)

The label associated with the RadioButton can be set after constructing with::

  radiobutton.set_label(label)

It is good practice to use a mnemonic in the label. This requires an underscore inserted into the label (e.g. "_Cancel"). GTK+ parses the underscore and converts it into an underline beneath the following character, which the user can then access as a shortcut to the function.

  radiobutton.set_use_underline(True)
  
.. note:

  Mnemonic shortcuts are highly useful as an accessibility feature and should be used wherever possible. They are particularly important to people with disabilities as they provide quick access to common functions. To access the function using the mnemonic, hold down :kbd:`ALT` and the appropriate character.

=======
Signals
=======
The commonly used signals of a RadioButton are::

  "toggled" (radiobutton)
  "group-changed" (radiobutton)

A ``"toggled"`` signal emits from the RadioButton when the mode is changed to active or inactive. When using this signal, you will need to check which RadioButton is receiving the active state. This is down to the ``"toggled"`` signal being emitted twice; once for the RadioButton becoming active and again for the RadioButton becoming inactive. The ``"group-changed"`` signal emits whenever a RadioButton changes which group it belongs to.

=======
Example
=======
Below is an example of a RadioButton:

.. literalinclude:: _examples/radiobutton.py

Download: :download:`RadioButton <_examples/radiobutton.py>`
