from datetime import datetime
from django.utils import timezone  # Fixed the previous timezone error!


class DatabaseManager:
    """A class to manage database connection states and tracking."""

    def __init__(self, db_name: str, db_user: str):
        """The constructor method. Initializes the object's properties."""
        self.db_name = db_name
        self.db_user = db_user
        self.is_connected = False
        self.last_sync_time = None

    def connect(self) -> str:
        """Changes the connection state to true."""
        self.is_connected = True
        return f"Successfully connected to database: '{self.db_name}' as user '{self.db_user}'."

    def sync_schema(self) -> dict:
        """Simulates a schema sync and tracks the execution time using timezone."""
        if not self.is_connected:
            return {"status": "Error", "message": "Cannot sync. Database is disconnected."}

        # Update tracking properties
        self.last_sync_time = timezone.now()

        return {
            "status": "Success",
            "synchronized_at": self.last_sync_time.strftime("%Y-%m-%d %H:%M:%S"),
            "tables_found": 12,
        }

    def disconnect(self) -> str:
        """Resets the connection state."""
        self.is_connected = False
        return f"Disconnected from '{self.db_name}'."
