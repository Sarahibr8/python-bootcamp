# Guided Lab — Model an Online Store

## Step 8 — on_delete Justifications

1. **Category → Category — SET_NULL**  
   If a parent category is deleted, the child category should remain but its parent relationship should be cleared.

2. **Product → Category — PROTECT**  
   A category should not be deleted while products still depend on it.

3. **CustomerProfile → User — CASCADE**  
   If a user is deleted, their customer profile should also be deleted.

4. **Order → User — CASCADE**  
   If a user is deleted, their orders should also be deleted.

5. **OrderItem → Order — CASCADE**  
   If an order is deleted, its order items should also be deleted because they belong to that order.

6. **OrderItem → Product — PROTECT**  
   A product should not be deleted while existing order items still reference it.

## Exit Ticket

### Why does quantity belong in OrderItem rather than Product or Order?

`quantity` belongs in `OrderItem` because it describes how many units of a specific product were included in a specific order, rather than being a permanent property of the product or the entire order.

## Lab Status

- Requirements 1–7: Completed
- Requirement 8: Completed
- Exit Ticket: Completed
- Migrations: Not run, as required by the lab
- `models.py`: Completed for the guided lab
