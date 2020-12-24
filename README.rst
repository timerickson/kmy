kmy KMyMoney_ data file reader
================================

Usage
------------
`kmy` is straightforward to use (Python 3 tested only) - e.g.

.. code-block:: python

    from kmy import kmy

    mm = kmy.Kmy.from_kmy_file('/path/to/your-money.kmy')

That's it! Then just use it as you wish!

.. code-block:: python

    print("User", "name", mm.user.name, "email", mm.user.email)
    print("FileInfo", "creationDate", mm.fileInfo.creationDate, "lastModifiedDate", mm.fileInfo.lastModifiedDate)
    print("Found", len(mm.institutions), "Institutions")
    print("Found", len(mm.accounts), "Accounts")
    print("Found", len(mm.transactions), "Transactions")
    print("Found", len(mm.tags), "Tags")
    print("Found", len(mm.payees), "Payees")
    print("Found", len(mm.costCenters), "CostCenters")

There are still some outliers like `tags` that are not yet implemented.
Feel free to submit Issues or MRs. It works for what I want for now, but
we shall see how or if it evolves :-)

.. _KMyMoney: https://kmymoney.org/