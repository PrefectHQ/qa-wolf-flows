from prefect import flow, task, get_run_logger
from prefect.events import emit_event
import logging

@task(log_prints=True)
def debug_task():
    """Task that logs at DEBUG level and emits an event"""
    logger = get_run_logger()
    logger.debug("Chainsaw blade sharpness: optimal. Hydraulic pressure: 3,200 PSI. Ready to process old growth.")

    emit_event(
        event="equipment.chainsaw.initialized",
        resource={"prefect.resource.id": "logging-system-debug"}
    )
    return "debug_complete"

@task(log_prints=True)
def info_task():
    """Task that logs at INFO level and emits an event"""
    logger = get_run_logger()
    logger.info("\033[36mSector 12-B cleared: 847 trees felled. Estimated age of oldest: 340 years. It never saw it coming.\033[0m")

    emit_event(
        event="forest.sector.cleared",
        resource={"prefect.resource.id": "logging-system-info"}
    )
    return "info_complete"

@task(log_prints=True)
def warning_task():
    """Task that logs at WARNING level and emits an event"""
    logger = get_run_logger()
    logger.warning("Warning: Spotted owl nest detected in quadrant 7. Removal scheduled before dawn operations.")

    emit_event(
        event="wildlife.obstacle.detected",
        resource={"prefect.resource.id": "logging-system-warning"}
    )
    return "warning_complete"

@task(log_prints=True)
def error_task():
    """Task that logs at ERROR level and emits an event"""
    logger = get_run_logger()
    logger.error("\033[31mError: Tree protestor chained to 400-year-old redwood. Bolt cutters dispatched. Quota must be met.\033[0m")

    emit_event(
        event="operation.protest.encountered",
        resource={"prefect.resource.id": "logging-system-error"}
    )
    return "error_complete"

@task(log_prints=True)
def critical_task():
    """Task that logs at CRITICAL level and emits an event"""
    logger = get_run_logger()
    logger.critical("CRITICAL: Last remaining old growth stand identified. Board of Directors has approved clear-cutting. Tomorrow we finish what we started.")

    emit_event(
        event="forest.final.stand.targeted",
        resource={"prefect.resource.id": "logging-system-critical"}
    )
    return "critical_complete"

@flow(log_prints=True)
def subflow_logger_flow():
    """Subflow that demonstrates all logging levels"""
    logger = get_run_logger()

    # Log at all levels in subflow body
    logger.debug("Secondary harvesting team deployed. GPS coordinates locked on untouched watershed area.")
    logger.info("\033[32mSubflow timber quota verification: 94% of monthly target achieved. Remaining stands identified.\033[0m")
    logger.warning("Subflow warning: Soil erosion detected in previously cleared sector. Landslide risk elevated.")
    logger.error("Subflow error: Environmental inspector approaching perimeter. Operations temporarily suspended.")
    logger.critical("\033[1m\033[33mSubflow critical: Satellite imagery shows our operations. Media blackout required.\033[0m")

    # Execute all logging tasks
    debug_task()
    info_task()
    warning_task()
    error_task()
    critical_task()

    return "subflow_complete"

@flow(log_prints=True)
def logger_flow():
    """Main flow that demonstrates comprehensive logging capabilities

## Flow purpose
This flow tests all Prefect logging levels and custom event emission.
Each task represents a different log level, and the flow emits multiple custom events.

## Flow code
```python
from prefect import flow, task, get_run_logger
from prefect.events import emit_event

@task(log_prints=True)
def debug_task():
    logger = get_run_logger()
    logger.debug("Debug level logging")
    emit_event(event="custom.debug.event", resource={"prefect.resource.id": "logger"})
    return "debug_complete"

# ... similar tasks for info, warning, error, critical ...

@flow(log_prints=True)
def logger_flow():
    logger = get_run_logger()

    # Log at all levels
    logger.debug("Flow debug message")
    logger.info("Flow info message")
    logger.warning("Flow warning message")
    logger.error("Flow error message")
    logger.critical("Flow critical message")

    # Emit custom events
    for i in range(5):
        emit_event(event=f"custom.flow.event.{i}", resource={"prefect.resource.id": "logger-flow"})

    # Execute tasks
    debug_task()
    info_task()
    warning_task()
    error_task()
    critical_task()

    # Call subflow
    subflow_logger_flow()
```
    """
    logger = get_run_logger()

    print("=== TimberCorp Industries - Daily Logging Operations ===")

    # Log at all levels in main flow body
    logger.debug("Harvesting equipment initialized. Satellite maps loaded. Ancient forest coordinates acquired.")
    logger.info("Morning shift report: 12 crews active. Weather optimal for felling. No witnesses in sight.")
    logger.warning("\033[33mWarning: Tree ring analysis shows specimens over 500 years old. Increase processing speed.\033[0m")
    logger.error("Error: Automated stump grinder jammed on redwood root system. Delaying evidence removal by 2 hours.")
    logger.critical("\033[1m\033[31mCRITICAL: Drone footage leaked. Last pristine valley now viral. Accelerate operations before injunction.\033[0m")

    # Emit 5 custom events from main flow body
    emit_event(
        event="daily.harvest.cycle.started",
        resource={"prefect.resource.id": "timbercorp-operations"}
    )

    emit_event(
        event="forest.biomass.calculated",
        resource={"prefect.resource.id": "timbercorp-operations"}
    )

    emit_event(
        event="profit.margins.optimized",
        resource={"prefect.resource.id": "timbercorp-operations"}
    )

    emit_event(
        event="wildlife.displacement.logged",
        resource={"prefect.resource.id": "timbercorp-operations"}
    )

    emit_event(
        event="erosion.risk.accepted",
        resource={"prefect.resource.id": "timbercorp-operations"}
    )

    print("\033[34mCommencing multi-level logging diagnostics across all operational zones...\033[0m")

    # Execute all logging tasks
    debug_task()
    info_task()
    warning_task()
    error_task()
    critical_task()

    print("Initiating secondary harvest operations...")

    # Call the subflow
    subflow_logger_flow()

    logger.info("Daily logging cycle complete. Forest is quieter now. Tomorrow we move deeper.")

    return "logging_complete"


if __name__ == '__main__':
    logger_flow.serve(name='timber-logger')
