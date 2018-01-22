# lithium_checksum_tool
`python3 lithium_checksum_tool.py`

Calculates Lithium radio checksum given a payload

Pseudocode from datasheet:

```
CK_A = 0, CK_B = 0
For(I=0;I<N;I++)
{
	CK_A = CK_A + Buffer[I]
	CK_B = CK_B + CK_A
}
```